import pandas as pd


class MissingValue:
    """
    this class is for the missing the values of the dataframe and
    we should find them and fill or remove them
    """

    def __init__(self, file) -> None:
        try:
            self.data = pd.read_csv(file)
        except FileNotFoundError:
            print("Error: File not found. Please check the file path.")
        except pd.errors.EmptyDataError:
            print("Error: The file is empty. Please check the file contents.")
        except pd.errors.ParserError:
            print("Error: Error parsing the file. Please check the file format.")

    def data_show_head(self, row: int = None):
        """
        this function is for a time that we want to showing the data frame to the user and now
        if user want to see the more than the default of the head , it can pass a number as input to the
        function
        Args:
            row (int, optional): a number can pass to the function for receving the dataframe row
        """
        return self.data.head(row)

    def data_frame_info(self):
        """
        this function is for showing the information of the dataframe
        """
        return self.data.info()

    def data_frame_shape(self):
        """
        this function is for showing the shape of the dataframe
        """
        return self.data.shape

    def data_columns(self):
        """
        this method is for a time that we want to bring all the columns
        """
        return self.data.columns.to_list()

    def data_isna_sum(self):
        """
        this function is for a time that we want to get the sum of the nall fields
        """
        return self.data.isna().sum()

    def data_unique_value(self, column: str):
        """
        this function is for retriving the unique value that is in the each column of the dataframe
        Args:
            column (str): name of the column that we have
        """
        try:
            result = self.data[column].unique()
            return result
        except:
            print("Missing some value")

    def find_data_isna_column(self, coulmn: str):
        """
        this function is for a time that we want to finding the isna from specific column
        Args:
            coulmn (str): specify the name of the column that we want to find its nall
        """
        result = self.data[self.data[coulmn].isna()]
        return result

    def fill_isna_column_max(self, column):
        """
        this method is for a time that we want to fill the isna column with max value of that column
        Args:
            columns (list): this is the list of columns that we want to fill the isna
        """
        self.data[column] = self.data[column].fillna(self.data[column].max())


    def fill_isna_column_string_type(self, column):
        """
        here in this method of missing value we fill the columns that type of them are string and 
        we fil them with empty string....
        """
        self.data[column] = self.data[column].fillna("")
        

    def fill_all_isna_columns(self):
        """
        in this method we fill all the isna clumns , if coulmn was bifc we fill it with max valure
        and if the column was string we fill it with empty qutation
        """
        for column in self.data_columns():
            if self.data[column].dtypes.kind == "bifc":
                self.fill_isna_column_max(column)
            else:
                self.fill_isna_column_string_type(column)
        return self.data

    def data_column_type(self, column) -> dict:
        """
        this function is for a time that we want to get the type of the column
        :param column:
            list of column names
        :return:
            dict where keys are column names and values are data types
        """
        cols_dict = {}
        for i in column:
            cols_dict[i] = self.data[i].dtypes
        return cols_dict

    def handle_missing_values(self):
        """
        this function is for a time that we want to fill the missing value
        :return:
        """
        missing_values = self.data_isna_sum().to_dict()

        if all(x == 0 for x in list(missing_values.values())):
            return self.data  # Return the original DataFrame if no missing values
        else:
            keys_with_missing_value = list(map(lambda x: x[0], filter(lambda x: x[1] == 1, missing_values.items())))

            miss_values_type = self.data_column_type(keys_with_missing_value)

            int_float_column = []
            string_column = []
            for k, v in miss_values_type.items():
                if v == int or v == float:
                    int_float_column.append(k)
                if v == object or v == str:
                    string_column.append(k)

            self.fill_isna_column_max(int_float_column)
            self.fill_isna_column_string_type(string_column)
            return self.data  # Return the updated DataFrame
