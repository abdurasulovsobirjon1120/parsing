from django.urls import path
from .views import AnimeSearchAPI

urlpatterns = [
    path('search/', AnimeSearchAPI.as_view(), name='anime-search'),
    # path('episodes/', AnimeEpisodesView.as_view(), name='anime-episodes'),
]
