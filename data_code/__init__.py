import pandas as pd
import io


class CSVReader:
    def __init__(self, file):
        """Read the CSV file into a pandas DataFrame."""
        try:
            self.file = file
            self.data = pd.read_csv(file)  # Read CSV from file stream
            print("Successfully read CSV file.")
        except Exception as e:
            print(f"Error reading the CSV file: {e}")

    def object_datatype(self):
        object_columns = self.data.select_dtypes(include=['object']).columns
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

    def data_info(self):
        # Create a temporary DataFrame to capture the info
        info = self.data.info()
        return info  # Return as string

    def data_describe(self):
        return self.data.describe()

    def columns(self):
        return self.data.columns.tolist()


# file = r'C:\Users\ae_sa\OneDrive\Desktop\working in django\Iris.csv'
# csv_reader = CSVReader(file)
#
# data_info = csv_reader.data_info()
# object_columns = csv_reader.object_datatype()
# describe = csv_reader.data_describe()

