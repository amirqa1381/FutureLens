from django.shortcuts import render
from django.http import HttpRequest
import io
import base64
from django.views import View
from data_code.prepare import CSVReader
from data_code.plot import Plotter

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


class ShowTheDataFrame(View):

    def get(self, request: HttpRequest):
        """
        this function is for the get method and when user send the get request this is come
        to this method
        Args:
            request (HttpRequest): _description_
        """
        file = r"/home/amir/django/data_analys/datas/titanic.csv"
        csv_reader = CSVReader(file)
        data_info = csv_reader.data_info()
        describe = csv_reader.data_describe()
        context = {
            "data_info": data_info,
            "describe": describe,
        }
        return render(request, "main/data_frame.html", context)



class ShowThePlot(View):
    """
    this class is for showing the plots in the page that we  want for better understanding
    and seperate them from the dataframe
    Args:
        View (django.views): this is the views
    """
    def get(self, request: HttpRequest):
        """
        this method is for the handling the get method for a time that user send the get request for 
        seeing the plot page
        Args:
            request (HttpRequest): _description_
        """
        file = r"/home/amir/django/data_analys/datas/titanic.csv"
        plotter = Plotter(file)
        distplot  = plotter.distplot(column='Age')
        histplot = plotter.hist(column='Age', hue='Survived')
        scatterplot = plotter.scatter(x='Survived', y='Age')
        print(distplot)
        context = {
            'displot': distplot,
            'histplot' : histplot,
            'scatterplot': scatterplot,
        }
        return render(request, 'main/plot.html', context)
     