import numpy as np
import pandas as pd


class PlotsInfo:
    def __init__(self, df):
        try:
            self.data = pd.read_csv(df)
            self.columns = self.data.columns.tolist()

            self.list_of_categories = []
            print("Successfully read CSV file.")
        except FileNotFoundError:
            print("Error: File not found. Please check the file path.")
        except pd.errors.EmptyDataError:
            print("Error: The file is empty. Please check the file contents.")
        except pd.errors.ParserError:
            print("Error: Error parsing the file. Please check the file format.")

    def data_column_type(self, column) -> dict:
        cols_dict = {}
        for i in column:
            cols_dict[i] = self.data[i].dtypes
        return cols_dict

    def cat(self):

        for col in self.data.columns:
            unique_values = set(self.data[col])

            if len(unique_values) < 10:
                self.list_of_categories.append(col)

    def columns_information(self):
        result = {}

        for col in self.list_of_categories:
            column_result = {'datatype': 'categorical'}
            result[col] = column_result
        for i in self.list_of_categories:
            self.columns.remove(i)


        for col in self.columns:
            column_result = {}
            if self.data.dtypes[col] in ['int', 'float']:
                column_result['datatype'] = 'numeric'
            elif self.data.dtypes[col] in ['object']:
                column_result['datetype'] = 'string'
            elif self.data.dtypes[col] == 'datetime64[ns]':
                column_result['datatype'] = 'datetime'
            else:
                column_result['data_type'] = 'unknown'
            result[col] = column_result
        return result
