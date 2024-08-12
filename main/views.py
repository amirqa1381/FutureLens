from django.shortcuts import render
from django.http import HttpRequest
import matplotlib.pyplot as plt
import numpy as np
import io
import urllib
import base64


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
