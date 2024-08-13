from django.shortcuts import render
from django.http import HttpRequest
import matplotlib.pyplot as plt
import numpy as np
import io
import base64
from data_code import read_file
from .forms import GetFile
import base64
from django.core.files.uploadedfile import InMemoryUploadedFile
import csv

def read(request: HttpRequest):
    data = read_file()
    to_html = data.to_html(classes='table table_striped', index=False)

    context = {"data": to_html}
    return render(request, 'main/data_show.html', context)


def index_view(request: HttpRequest):
    """
    this function is for the index view and we can show the all the chart on it for the starting
    Args:
        request (HttpRequest): this is the request that we pass to this function
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


def getting_form(request: HttpRequest):
    if request.method == 'GET':
        form = GetFile()
        context = {
            'form': form
        }
        return render(request, 'main/getting_file.html', context)
    elif request.method == "POST":
        csv_data = []
        form = GetFile(request.POST)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            if uploaded_file.name.endswith('.csv'):
                csv_file = io.TextIOWrapper(uploaded_file.file, encoding='utf-8')
                reader = csv.reader(csv_file)
                for row in reader:
                    csv_data.append(row)
            return render(request, 'main/getting_file.html', {'csv_data': csv_data})
        context = {
            'form': form
        }
        return render(request, 'main/getting_file.html', context)
        
            
            