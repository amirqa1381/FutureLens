from django.urls import path
from .views import IndexView, ShowTheDataFrame, ShowThePlot


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('data-frame/', ShowTheDataFrame.as_view(), name='data-frame'),
    path('plot/', ShowThePlot.as_view(), name='show_plot'),
]
