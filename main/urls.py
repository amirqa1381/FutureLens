from django.urls import path
from .views import (IndexView,
                    ShowTheDataFrame,
                    ShowThePlot,
                    UploadTheFile,
                    UserDatasListView,
                    ImplementingMissingAndFixingData,
                    )


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('data-frame/<slug:slug>', ShowTheDataFrame.as_view(), name='data-frame'),
    path('plot/<slug:slug>', ShowThePlot.as_view(), name='show_plot'),
    path("upload-file/", UploadTheFile.as_view(), name="uploading_file"),
    path("datas-list/", UserDatasListView.as_view(), name="data-list"),
    path("fix-data/", ImplementingMissingAndFixingData.as_view(), name="fix_data"),
]
