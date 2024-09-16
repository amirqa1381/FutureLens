from django.urls import path
from .views import (IndexView,
                    ShowTheDataFrame,
                    ShowThePlot,
                    UploadTheFile,
                    )


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('data-frame/<slug:slug>', ShowTheDataFrame.as_view(), name='data-frame'),
    path('plot/', ShowThePlot.as_view(), name='show_plot'),
    path("upload-file/", UploadTheFile.as_view(), name="uploading_file"),
]
