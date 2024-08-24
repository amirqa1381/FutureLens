from django.shortcuts import render
from django.http import HttpRequest
import matplotlib.pyplot as plt
import numpy as np
import io
import base64
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.views import View
from data_code import CSVReader


class IndexView(View):
    """
    this is the main class that we have for showing the main page for project

    Args:
        View (.views): this is the class that i inherited from it
    """

    def get(self, request: HttpRequest):
        """
        this function is the get method and is for handling the get method for routing it
        """
        return render(request, "main/index.html")

    def post(self, request: HttpRequest):
        """
        this function is the post method and is for handling the post method for routing it
        """
        pass


class ShowTheChart(View):

    def get(self, request: HttpRequest):
        """
        this function is for the get method and when user send the get request this is come
        to this method
        Args:
            request (HttpRequest): _description_
        """
        file = r"/home/amir/django/data_analys/datas/train.csv"
        csv_reader = CSVReader(file)
        data_info = csv_reader.data_info()
        object_columns = csv_reader.object_datatype()
        describe = csv_reader.data_describe()
        displot = csv_reader.displot(x_column="temp", hue_column="workingday")
        catplot = csv_reader.catplot(
            x_column="season", y_column="count", hue_column="count"
        )
        hisplot = csv_reader.histplot(x_column="windspeed", hue_column="season")
        scatter = csv_reader.scatterplot(
            x_column="windspeed", y_column="count", hue_column="season"
        )
        context = {
            "data_info": data_info,
            "object_columns": object_columns,
            "describe": describe,
            "displot": displot,
            "catplot": catplot,
            "hisplot": hisplot,
            "scatter": scatter,
        }
        return render(request, "main/chart.html", context)

    def post(self, request: HttpRequest):
        """
        this function is for the post method and when user send the post request this is come
        to this method
        Args:
            request (HttpRequest): _description_
        """
        pass


# def read(request: HttpRequest):
#     data = read_file()
#     to_html = data.to_html(classes="table table_striped", index=False)

#     context = {"data": to_html}
#     return render(request, "main/data_show.html", context)


# def getting_form(request: HttpRequest):
#     if request.method == "GET":
#         form = GetFile()
#         context = {"form": form}
#         return render(request, "main/getting_file.html", context)
#     elif request.method == "POST":
#         form = GetFile(request.POST, request.FILES)
#         if form.is_valid():
#             uploaded_file = form.cleaned_data["file"]
#             data = read_file(uploaded_file)
#             print(data)
#             to_html = data.to_html(classes="table table_striped", index=False)
#             request.session['data_html'] = to_html
#             context = {
#                 "to_html": to_html,
#             }
#             print("Successfull")
#             return render(request, "main/user_upload_show.html", context)
#         else:
#             context = {"form": form}
#             return render(request, "main/getting_file.html", context)
#     # handel the button click
#     if 'another_button' in request.POST:
#         to_html = request.session.get('data_html', None)
#         result = columns()
#         context = {
#             'to_html': to_html,
#             'result':result
#         }
#         return render(request, 'main/user_upload_show.html',context)
