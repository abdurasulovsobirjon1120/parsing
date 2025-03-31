from django.urls import path
from .views import AnimePaheSearchView

urlpatterns = [
    path('search/', AnimePaheSearchView.as_view(), name='anime-search'),
    # path('episodes/', AnimeEpisodesView.as_view(), name='anime-episodes'),
]
