from rest_framework import serializers
from .models import Anime, Episode, VideoServer

class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = "__all__"

class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = "__all__"

class VideoServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoServer
        fields = "__all__"
