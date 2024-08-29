from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.views import View
from data_code.prepare import CSVReader
from data_code.plot import Plotter, get_specific_method_name, get_length_of_methods
from django.contrib import messages

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
        checked_input = request.POST.getlist('column')
        print(checked_input)
        return redirect('data-frame')


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
        data_column = csv_reader.data_column()
        context = {
            "data_info": data_info,
            "describe": describe,
            "data_column": data_column,
        }
        return render(request, "main/data_frame.html", context)
    
    def post(self, request: HttpRequest):
        """
        this is a function that is for handling the post request and if user submit simething it will handle 
        it....
        Args:
            request (HttpRequest): _description_

        Returns:
            _type_: _description_
        """
        checked_items = request.POST.getlist("columns[]")
        if len(checked_items) > 2:
            messages.error(request, f"You should select two items, but you've selected {len(checked_items)}")
        else:
            messages.success(request, f"The items was added successfully")
        return redirect('data-frame')



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
        methods = get_length_of_methods(Plotter, "plot")
        context = {
            "methods": methods,
        }
        return render(request, "main/plot.html", context)
     