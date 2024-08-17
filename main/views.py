from django.shortcuts import render
from django.http import HttpRequest
import matplotlib.pyplot as plt
import numpy as np
import io
import base64
from data_code import read_file, columns
from .forms import GetFile
import base64
from django.core.files.uploadedfile import InMemoryUploadedFile
import csv
from django.views import View


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
        # sample data
        x = np.linspace(0, 10, 100)
        y = np.sin(x)

        # create the plot
        plt.figure()
        plt.plot(x, y)
        plt.title("Sine Wave")
        plt.xlabel("x-axis")
        plt.ylabel("Y-axis")

        # save the plot to the bytesIO object
        buf = io.BytesIO()
        plt.savefig(buf, format="png")
        plt.close()
        buf.seek(0)

        # Encode the image to base64
        image_png = base64.b64encode(buf.read())
        buf.close()
        image_str = image_png.decode("utf-8")
        context = {"chart": image_str}
        return render(request, "main/index.html", context)
    
    def post(self, request:HttpRequest):
        """
        this function is the post method and is for handling the post method for routing it
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


