from django.db import models

class Anime(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    anime_id = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.title

class Episode(models.Model):
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, related_name="episodes")
    episode_number = models.IntegerField()
    episode_id = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.anime.title} - Episode {self.episode_number}"

class VideoServer(models.Model):
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE, related_name="video_servers")
    server_name = models.CharField(max_length=100)
    video_url = models.URLField()

    def __str__(self):
        return f"{self.episode.anime.title} - Ep {self.episode.episode_number} ({self.server_name})"
