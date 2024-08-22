import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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

    def plot_distribution(self):
        if 'count' in self.data.columns:
            sns.displot(data=self.data, x='count', hue='workingday', kind='kde', fill=True)
            plt.title('Count Distribution by Working Day')
            plt.xlabel('Count')
            plt.ylabel('Density')
            plt.show()
        else:
            print("The 'count' column does not exist in the DataFrame.")
        # plt.figure(figsize=(15, 8))
        # sns.displot(self.data, x='count', hue='weather', kind='kde', palette='pastel')
        # plt.show()


file = r'datas/train.csv'
csv_reader = CSVReader(file)

# data_info = csv_reader.data_info()
# object_columns = csv_reader.object_datatype()
# describe = csv_reader.data_describe()
plot = csv_reader.plot_distribution()
print(plot)

