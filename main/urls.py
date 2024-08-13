from django.urls import path
from .views import index_view, read


urlpatterns = [
    path('', index_view, name='index'),
    path('show/', read)
]
