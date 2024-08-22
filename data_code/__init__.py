import sys
import base64
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io


class CSVReader:
    def __init__(self, file):
        """Read the CSV file into a pandas DataFrame."""
        self.data = pd.read_csv(file)  # Read CSV from file stream
        print("Successfully read CSV file.")

    def data_info(self):
        # Create a temporary DataFrame to capture the info
        buffer = io.StringIO()
        sys.stdout = buffer
        self.data.info()
        sys.stdout = sys.__stdout__
        info = buffer.getvalue()
        # info = self.data.info()
        return info  # Return as string

    def data_describe(self):
        return self.data.describe()

    def convert_to_html(self):
        """
        Converts the DataFrame to an HTML table.

        Returns:
            str: HTML representation of the DataFrame.
        """
        try:
            # Convert DataFrame to HTML
            html_table = self.data.to_html(classes="table table-striped", index=False)
            return html_table
        except Exception as e:
            print(f"An error occurred while converting to HTML: {e}")
            return None

    def object_datatype(self):
        object_columns = self.data.select_dtypes(include=["object"]).columns
        return object_columns.tolist()

    def isna(self):
        if self.data.isna().any().any():
            return self.data.columns[self.data.isna().any()].tolist()
        else:
            return False

    def dropna(self):
        na_columns = self.isna()
        if na_columns:
            self.data.drop(na_columns, axis=1, inplace=True)
            return na_columns
        else:
            return False

    def columns(self):
        return self.data.columns.tolist()

    def plot_distribution(self):
        if "count" in self.data.columns:
            sns.displot(
                data=self.data, x="count", hue="workingday", kind="kde", fill=True
            )
            plt.title("Count Distribution by Working Day")
            plt.xlabel("Count")
            plt.ylabel("Density")
        else:
            print("The 'count' column does not exist in the DataFrame.")

    import base64

    def displot(self, x_column, hue_column=None):
        """
        Creates a displot for the specified x_column.

        Parameters:
            x_column (str): The column to plot.
            hue_column (str or None): The column to use for color encoding.
        """
        try:
            sns.displot(self.data, x=x_column, hue=hue_column, kind="kde", fill=True)
            plt.title(f"Distribution plot of {x_column}")
            plt.xlabel(x_column)
            plt.ylabel("Density")
            img = io.BytesIO()
            plt.savefig(img, format="png")
            img.seek(0)
            img_b64 = base64.b64encode(img.getvalue()).decode("utf-8")
            return img_b64
        except Exception as e:
            print(f"An error occurred while creating displot: {e}")

    def catplot(self, x_column, y_column, hue_column=None):
        """
        Creates a catplot for the specified x_column and y_column.

        Parameters:
            x_column (str): The column to plot on the x-axis.
            y_column (str): The column to plot on the y-axis.
            hue_column (str or None): The column to use for color encoding.
        """
        try:
            sns.catplot(
                x=x_column, y=y_column, hue=hue_column, data=self.data, kind="strip"
            )
            plt.title(f"Categorical plot of {y_column} vs {x_column}")
            image = io.BytesIO()
            plt.savefig(image, format="png")
            image.seek(0)
            image_bs64 = base64.b64encode(image.getvalue()).decode("utf-8")
            return image_bs64
        except Exception as e:
            print(f"An error occurred while creating catplot: {e}")

    def histplot(self, x_column, hue_column=None):
        """
        Creates a histogram for the specified x_column.

        Parameters:
            x_column (str): The column to plot.
            hue_column (str or None): The column to use for color encoding.
        """
        try:
            sns.histplot(self.data, x=x_column, hue=hue_column, bins=30, kde=True)
            plt.title(f"Histogram of {x_column}")
            plt.xlabel(x_column)
            plt.ylabel("Count")
            img = io.BytesIO()
            plt.savefig(img, format='png')
            img.seek(0)
            img_bs64 = base64.b64encode(img.getvalue()).decode('utf-8')
            return img_bs64
        except Exception as e:
            print(f"An error occurred while creating histplot: {e}")

    def scatterplot(self, x_column, y_column, hue_column=None):
        """
        Creates a scatter plot for the specified x_column and y_column.

        Parameters:
            x_column (str): The column to plot on the x-axis.
            y_column (str): The column to plot on the y-axis.
            hue_column (str or None): The column to use for color encoding.
        """
        try:
            sns.scatterplot(data=self.data, x=x_column, y=y_column, hue=hue_column)
            plt.title(f"Scatter plot of {y_column} vs {x_column}")
            plt.xlabel(x_column)
            plt.ylabel(y_column)
            img = io.BytesIO()
            plt.savefig(img, format='png')
            img.seek(0)
            img_b64 = base64.b64encode(img.getvalue()).decode('utf-8')
            return img_b64
        except Exception as e:
            print(f"An error occurred while creating scatterplot: {e}")


# file = r'../../djda/datas/train.csv'
# csv_reader = CSVReader(file)
# csv_reader.displot(x_column='temp', hue_column='workingday')
# csv_reader.catplot(x_column='season', y_column='count', hue_column='count')
# csv_reader.histplot(x_column='windspeed', hue_column='season')
# csv_reader.scatterplot(x_column='windspeed', y_column='count', hue_column='season')
# data_info = csv_reader.data_info()
# info = csv_reader.data_info()
# print(info)
# # object_columns = csv_reader.object_datatype()
# print(info)
# describe = csv_reader.data_describe()
# plot = csv_reader.plot_distribution()
# print(plot)


# html = csv_reader.convert_to_html()
# print(html)
