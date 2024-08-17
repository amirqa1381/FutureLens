from django.urls import path
from .views import IndexView, ShowTheChart


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('chart/', ShowTheChart.as_view(), name='show_chart'),
]
