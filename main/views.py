from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.views import View
from data_code.prepare import CSVReader
from data_code.plot import Plotter, get_length_of_methods
from django.contrib import messages
from .forms import UploadedFile
from django.core.files.storage import FileSystemStorage


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
        form = UploadedFile()
        context = {"form": form}
        return render(request, "main/index.html", context)

    def post(self, request: HttpRequest):
        """
        this function is the post method and is for handling the post method for routing it
        """
        form = UploadedFile(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']  # Remove subscripting
            fs = FileSystemStorage(location="media/uploaded-file")
            filename = fs.save(file.name, file)
            uploaded_file_url = fs.url(filename)
            messages.success(request, "The file was successfully uploaded")
            return redirect("index")
        else:
            for error in form.errors.values():
                for message in error:
                    messages.error(request, message)
            context = {
                "form": form,
            }
            return render(request, "main/index.html", context)


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
        return redirect("data-frame")


class ShowThePlot(View):
    """
    this class is for showing the plots in the page that we  want for better understanding
    and seperate them from the dataframe
    Args:
        View (django.views): this is the views
    """

    file = r"/home/amir/django/data_analys/datas/titanic.csv"

    def get(self, request: HttpRequest):
        """
        this method is for the handling the get method for a time that user send the get request for
        seeing the plot page
        Args:
            request (HttpRequest): _description_
        """
        csv_reader = CSVReader(self.file)
        methods = get_length_of_methods(Plotter, "plot")
        data_column = csv_reader.data_column()
        context = {
            "methods": methods,
            "data_column": data_column,
        }
        return render(request, "main/plot.html", context)

    def post(self, request: HttpRequest):
        """
        this is the method in the class that is for the handling the post requesst

        Args:
            request (HttpRequest): _description_
        """
        plotter = Plotter(self.file)
        # here i've got the methods name and length of their params
        methods = get_length_of_methods(Plotter, "plot")
        checked_items = request.POST.getlist("columns[]")
        chosen_method = request.POST.get("method_name")
        if chosen_method in methods:
            # here with this function i've get the method that we should call and use
            method = getattr(plotter, chosen_method)
            if len(checked_items) != methods[chosen_method]:
                messages.error(
                    request,
                    f"The columns that you've chose is {len(checked_items)} but you should insert {methods[chosen_method]}",
                )
            else:
                # here i unpack the items that user passed for giving them to the method
                result = method(*checked_items)
                messages.success(request, "The Plot has correctly submitted")
                context = {
                    "chosen_method": chosen_method,
                    "result": result,
                }
                return render(request, "main/specific_plot.html", context)
        return redirect("show_plot")
