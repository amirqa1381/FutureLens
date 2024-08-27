import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64

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

    def hist(self, column, hue=None):
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

    def scatter(self, x, y, hue=None):
        try:
            plt.scatter(self.data[x], self.data[y], color=hue)
            plt.xlabel(x)
            plt.ylabel(y)
            plt.title(f'Scatter Plot of {x} vs {y}')
            buffer = io.BytesIO()
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            plot_url = base64.b64encode(buffer.getvalue()).decode('utf-8')
            return plot_url
        except AttributeError:
            print("Error: No data available. Please load the data first.")
        except KeyError:
            print("Error: Column not found. Please check the column names.")

    def bar(self, x, y):
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

    def heatmap(self):
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


file = r"C:\Users\ae_sa\OneDrive\Desktop\data scientist\data analysis\data sets\titanic\titanic.csv"
plotter = Plotter(file)
plotter.data_column()

