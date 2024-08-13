from django.urls import path
from .views import index_view, read, getting_form


urlpatterns = [
    path('', index_view, name='index'),
    path('show/', read), 
    path('getting-file/', getting_form, name='getting_file'),
]
