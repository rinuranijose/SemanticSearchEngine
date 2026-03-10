from django.urls import path
from .views import keyword_search, semantic_search

urlpatterns = [
    path("search/keyword", keyword_search),
    path("search/semantic", semantic_search),
]