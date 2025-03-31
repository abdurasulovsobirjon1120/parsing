import requests
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

BASE_URL = "https://animepahe.com/api"


class AnimePaheSearchView(APIView):
    def post(self, request):
        """
        Foydalanuvchi anime nomini POST orqali jo‘natadi,
        biz esa API orqali qidiramiz va natijani qaytaramiz.
        """
        query = request.data.get("query")  # POST so‘rovdan ma'lumot olish
        if not query:
            return Response({"error": "Query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

        url = f"{BASE_URL}?m=search&q={query}"
        response = requests.get(url)

        if response.status_code == 200:
            return Response(response.json())  # Topilgan natijalarni qaytarish
        return Response({"error": "Failed to fetch data"}, status=response.status_code)


class AnimePaheEpisodesView(APIView):
    def get(self, request, anime_id):
        page = request.GET.get("page", 1)
        url = f"{BASE_URL}?m=release&id={anime_id}&page={page}"
        response = requests.get(url)

        if response.status_code == 200:
            return Response(response.json())
        return Response({"error": "Failed to fetch episodes"}, status=response.status_code)


class AnimePaheVideoServersView(APIView):
    def get(self, request, episode_id):
        url = f"{BASE_URL}?m=links&id={episode_id}"
        response = requests.get(url)

        if response.status_code == 200:
            return Response(response.json())
        return Response({"error": "Failed to fetch video servers"}, status=response.status_code)
