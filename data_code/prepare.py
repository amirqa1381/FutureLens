import pandas as pd

class CSVReader:
    def __init__(self, file):
        """Read the CSV file into a pandas DataFrame."""
        self.data = pd.read_csv(file)  # Read CSV from file stream
        print("Successfully read CSV file.")

    def data_head(self):
        """Get the first 5 row of the CSV file."""
        dfhead = self.data.head()
        return dfhead

    def data_tail(self):
        """Get the last 5 row of the CSV file."""
        dftail = self.data.tail()
        return dftail

    def data_data_shape(self):
        dfshape = self.data.shape()
        return dfshape

    def data_count(self):
        """Get the number of rows for each column."""
        dfcount = self.data.count()
        return dfcount

    def data_describe(self):
        """
            Show some information about the data.

            Such as mean, max, std and quarters
        """
        dfdescribe = self.data.describe()
        return dfdescribe

    def data_info(self):
        """Show type of each column."""
        dfinfo = self.data.info()
        return dfinfo

    def data_var(self):
        """Show variance of the data."""
        dfvar = self.data.var()
        return dfvar

    def data_column(self):
        """Desplay the column names as list."""
        dfcolumn = self.data.columns.tolist()
        return dfcolumn

    def data_show_selected_columns(self, columns, row=5):
        """Display the selected columns and rows as data frame."""
        print(row)
        dfshow = self.data[columns][:row]
        return dfshow

    def data_value_counts(self, column, percentage=False):
        """Display the count of each column."""
        dfvalue_counts = self.data[column].value_counts(normalize=percentage)
        return dfvalue_counts

    def data_crosstab(self, col1, col2):
        """Display the frequency counts of combinations of two or more categorical variables."""
        dfcrosstab = pd.crosstab(self.data[col1], self.data[col2])
        return dfcrosstab

    def data_groupby(self, col):
        """Display group data by one or more columns """
        dfgroupby = self.data.groupby([col[0], col[1]])[col[2]].max()
        return dfgroupby

