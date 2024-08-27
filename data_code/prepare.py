import pandas as pd

class CSVReader:
    def __init__(self, file):
        """Read the CSV file into a pandas DataFrame."""
        try:
            self.data = pd.read_csv(file)  # Read CSV from file stream
            print("Successfully read CSV file.")
        except FileNotFoundError:
            print("Error: File not found. Please check the file path.")
        except pd.errors.EmptyDataError:
            print("Error: The file is empty. Please check the file contents.")
        except pd.errors.ParserError:
            print("Error: Error parsing the file. Please check the file format.")

    def data_head(self):
        """Get the first 5 rows of the CSV file."""
        try:
            dfhead = self.data.head()
            return dfhead
        except AttributeError:
            print("Error: No data available. Please load the data first.")

    def data_tail(self):
        """Get the last 5 rows of the CSV file."""
        try:
            dftail = self.data.tail()
            return dftail
        except AttributeError:
            print("Error: No data available. Please load the data first.")

    def data_shape(self):
        """Get the shape of the DataFrame."""
        try:
            dfshape = self.data.shape
            return dfshape
        except AttributeError:
            print("Error: No data available. Please load the data first.")

    def data_count(self):
        """Get the total number of rows."""
        try:
            dfcount = self.data.shape[0]
            return dfcount
        except AttributeError:
            print("Error: No data available. Please load the data first.")

    def data_describe(self):
        """
        Show some information about the data.

        Such as mean, max, std, and quarters
        """
        try:
            dfdescribe = self.data.describe()
            return dfdescribe
        except AttributeError:
            print("Error: No data available. Please load the data first.")

    def data_info(self):
        """Show type of each column."""
        try:
            dfinfo = self.data.info()
            return dfinfo
        except AttributeError:
            print("Error: No data available. Please load the data first.")

    def data_var(self):
        """Show variance of the data."""
        try:
            dfvar = self.data.var()
            return dfvar
        except AttributeError:
            print("Error: No data available. Please load the data first.")

    def data_column(self):
        """Display the column names as a list."""
        try:
            dfcolumn = self.data.columns.tolist()
            return dfcolumn
        except AttributeError:
            print("Error: No data available. Please load the data first.")

    def show_selected_columns(self, columns, row=5):
        """Display the selected columns and rows as a DataFrame."""
        try:
            dfshow = self.data[columns].head(row)
            return dfshow
        except AttributeError:
            print("Error: No data available. Please load the data first.")
        except KeyError:
            print("Error: Column not found. Please check the column names.")

    def data_value_counts(self, column, percentage=False):
        """Display the count of each column."""
        try:
            dfvalue_counts = self.data[column].value_counts(normalize=percentage)
            return dfvalue_counts
        except AttributeError:
            print("Error: No data available. Please load the data first.")
        except KeyError:
            print("Error: Column not found. Please check the column names.")

    def data_crosstab(self, col1, col2):
        """Display the frequency counts of combinations of two or more categorical variables."""
        try:
            dfcrosstab = pd.crosstab(self.data[col1], self.data[col2])
            return dfcrosstab
        except AttributeError:
            print("Error: No data available. Please load the data first.")
        except KeyError:
            print("Error: Column not found. Please check the column names.")

    def data_groupby(self, col):
        """Display group data by one or more columns."""
        try:
            dfgroupby = self.data.groupby(col).max()
            return dfgroupby
        except AttributeError:
            print("Error: No data available. Please load the data first.")
        except KeyError:
            print("Error: Column not found. Please check the column names.")

