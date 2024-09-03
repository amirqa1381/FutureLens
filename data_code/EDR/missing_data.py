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
    


file = r"../../datas/Cust_Segmentation.csv"
missing = MissingValue(file=file)
# print(missing.data_frame_info())
# print(missing.data_isna_sum())
# print(missing.data_show_head(5))
print(missing.data_unique_value())
