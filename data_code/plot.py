import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64
import inspect


class Plotter:
    def __init__(self, file):
        """Read the CSV file into a pandas DataFrame."""
        try:
            self.data = pd.read_csv(file)
            print("Successfully read CSV file.")
        except FileNotFoundError:
            print("Error: File not found. Please check the file path.")
        except pd.errors.EmptyDataError:
            print("Error: The file is empty. Please check the file contents.")
        except pd.errors.ParserError:
            print("Error: Error parsing the file. Please check the file format.")

    def data_column(self):
        """Display the column names as a list."""
        try:
            dfcolumn = self.data.columns.tolist()
            return dfcolumn
        except AttributeError:
            print("Error: No data available. Please load the data first.")

    def plot(self, x, y, hue=None):
        try:
            plt.plot(self.data[x], self.data[y], color=hue)
            plt.xlabel(x)
            plt.ylabel(y)
            plt.title(f'Plot of {x} vs {y}')
            buffer = io.BytesIO()
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            plot_url = base64.b64decode(buffer.getvalue()).decode()
            return plot_url
        except AttributeError:
            print("Error: No data available. Please load the data first.")
        except KeyError:
            print("Error: Column not found. Please check the column names.")

    def histplot(self, column, hue=None):
        try:
            sns.histplot(data=self.data, x=column, hue=hue)
            plt.xlabel(column)
            plt.ylabel('Frequency')
            plt.title(f'Histogram of {column}')
            buffer = io.BytesIO()
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            plot_url = base64.b64encode(buffer.getvalue()).decode('utf-8')
            return plot_url
        except AttributeError:
            print("Error: No data available. Please load the data first.")
        except KeyError:
            print("Error: Column not found. Please check the column names.")

    def scatterplot(self, x, y, hue=None):
        try:
            plt.scatter(self.data[x], self.data[y], c=self.data[hue])
            plt.xlabel(x)
            plt.ylabel(y)
            plt.title(f'Scatter Plot of {x} vs {y}')
            buffer = io.BytesIO()
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            plot_url = base64.b64encode(buffer.getvalue()).decode('utf-8')
            return  plot_url
        except AttributeError:
            print("Error: No data available. Please load the data first.")
        # except KeyError:
        #     print("Error: Column not found. Please check the column names.")

    def barplot(self, x, y):
        try:
            plt.bar(self.data[x], self.data[y])
            plt.xlabel(x)
            plt.ylabel(y)
            plt.title(f'Bar Chart of {x} vs {y}')
            buffer = io.BytesIO()
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            plot_url = base64.b64decode(buffer.getvalue()).decode()
            return plot_url
        except AttributeError:
            print("Error: No data available. Please load the data first.")
        except KeyError:
            print("Error: Column not found. Please check the column names.")

    def boxplot(self):
        try:
            print(self.data.dtypes)
            plt.boxplot(self.data.values)
            plt.title('Box Plot')
            buffer = io.BytesIO()
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            plot_url = base64.b64decode(buffer.getvalue()).decode()
            return plot_url
        except AttributeError:
            print("Error: No data available. Please load the data first.")
        except KeyError:
            print("Error: Column not found. Please check the column names.")

    def pairplot(self):
        try:
            sns.pairplot(self.data)
            plt.title('Pair Plot')
            buffer = io.BytesIO()
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            plot_url = base64.b64decode(buffer.getvalue()).decode()
            return plot_url
        except AttributeError:
            print("Error: No data available. Please load the data first.")
        except KeyError:
            print("Error: Column not found. Please check the column names.")

    def countplot(self, column):
        try:
            sns.countplot(x=column, data=self.data)
            plt.title(f'Count Plot of {column}')
            buffer = io.BytesIO()
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            plot_url = base64.b64decode(buffer.getvalue()).decode()
            return plot_url
        except AttributeError:
            print("Error: No data available. Please load the data first.")
        except KeyError:
            print("Error: Column not found. Please check the column names.")

    def distplot(self, column):
        try:
            sns.distplot(self.data[column])
            plt.title(f'Distribution Plot of {column}')
            # here i've created a buffer for read and write 
            buffer = io.BytesIO()
            # saving the plot fig
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            # here i've encode the buffer for showing it in the template
            plot_url = base64.b64encode(buffer.getvalue()).decode()
            return plot_url
        except AttributeError:
            print("Error: No data available. Please load the data first.")
        except KeyError:
            print("Error: Column not found. Please check the column names.")

    def heatmapplot(self):
        try:
            sns.heatmap(self.data.corr(), annot=True, cmap='coolwarm', square=True)
            plt.title('Heatmap')
            buffer = io.BytesIO()
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            plot_url = base64.b64encode(buffer.getvalue()).decode()
            return plot_url
        except AttributeError:
            print("Error: No data available. Please load the data first.")


def get_specific_method_name(cls , substring: str):
    """
    here we get the class name and we bring the all the methods that has substring on it
    Args:
        sustring (string): a string that we pass for get the methods that have this substring on it
    """
    search_result = [name for name , _ in inspect.getmembers(cls, predicate=inspect.isfunction) if substring in name]
    return search_result



def get_length_of_methods(cls , substring: str):
    """
    this function is for checking the length of the parameter of each method and we can get lengeth of the
    paramater of each method
    """
    method_param_length = {}
    list_of_methods = get_specific_method_name(cls , substring)
    for name in list_of_methods:
        # here i retrived the method from the class and if method does not exist in the class it returns None
        method = getattr(cls, name, None)
        # here we checked that the method that we retrived is callable or not
        if callable(method):
            # here we just get the all the params that is passed to a function 
            params = inspect.signature(method).parameters
            # here after removing the self parameter from the function we calculate the length of all params
            param_length = len([param for param in params if param != "self"])
            # pass the name of the mathod and length of it to the dictionary 
            method_param_length[name] = param_length
        else:
            method_param_length[name] = "Method is not callable"
    return method_param_length          


