from django.urls import path
from .views import IndexView, ShowTheDataFrame, ShowThePlot


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('chart/', ShowTheDataFrame.as_view(), name='show_chart'),
    path('plot/', ShowThePlot.as_view(), name='show_plot'),
]
