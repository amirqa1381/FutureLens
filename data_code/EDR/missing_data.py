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

    def fill_isna_column_max(self, column: str) -> None:
        """
        this method is for a time that we want to fill the isna column with max value of that coulmn
        Args:
            column (str): this is the column that we want to fill the isna
        """
        self.data[column] = self.data[column].fillna(self.data[column].max())

    def fill_isna_column_string_type(self, column: str) -> None:
        self.data[column] = self.data[column].fillna("")

    def data_columns(self):
        """
        this method is for a time that we want to bring all the columns
        """
        
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


