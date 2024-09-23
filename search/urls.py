from django.urls import path
from .views import search_view, search_result

urlpatterns = [
    path('', search_view, name="search"),
    path("se/results/<str:token>", search_result, name='search_results'),
]
