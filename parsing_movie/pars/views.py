from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://animepahe.ru/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

class AnimeSearchAPI(APIView):
    def post(self, request, *args, **kwargs):
        if not request.content_type == "application/json":
            return Response({"error": "Content-Type application/json bo‘lishi kerak"}, status=status.HTTP_400_BAD_REQUEST)

        query = request.data.get("q", "").strip()
        if not query:
            return Response({"error": "Anime nomini kiriting!"}, status=status.HTTP_400_BAD_REQUEST)

        # 🔍 1. Anime qidirish
        search_url = f"{BASE_URL}search?keyword={query}"
        response = requests.get(search_url, headers=HEADERS)
        if response.status_code != 200:
            return Response({"error": "Anime ma'lumotlarini yuklab bo‘lmadi."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        soup = BeautifulSoup(response.text, "html.parser")
        anime_results = soup.find_all("div", class_="col-xl-3 col-lg-4 col-md-6 col-sm-6 col-12")

        if not anime_results:
            return Response({"error": "Hech qanday natija topilmadi."}, status=status.HTTP_404_NOT_FOUND)

        anime_list = []
        for anime in anime_results:
            title = anime.find("h2").text.strip()
            anime_url = anime.find("a")["href"]
            full_anime_url = f"{BASE_URL}{anime_url}"

            # 🔍 2. Epizodlar sahifasini ochish
            anime_page = requests.get(full_anime_url, headers=HEADERS)
            if anime_page.status_code != 200:
                continue

            anime_soup = BeautifulSoup(anime_page.text, "html.parser")
            episodes = anime_soup.find_all("div", class_="episode")

            episode_list = []
            for ep in episodes:
                ep_number = ep.find("div", class_="episode-number").text.strip()
                ep_url = ep.find("a")["href"]
                full_ep_url = f"{BASE_URL}{ep_url}"

                # 🔍 3. Epizod videosini olish
                ep_page = requests.get(full_ep_url, headers=HEADERS)
                if ep_page.status_code != 200:
                    continue

                ep_soup = BeautifulSoup(ep_page.text, "html.parser")
                video_links = ep_soup.find_all("a", class_="video-source")

                video_urls = []
                for link in video_links:
                    video_urls.append(link["href"])

                episode_list.append({
                    "episode_number": ep_number,
                    "video_urls": video_urls
                })

            anime_list.append({
                "title": title,
                "episodes": episode_list
            })

        return Response({"results": anime_list}, status=status.HTTP_200_OK)
