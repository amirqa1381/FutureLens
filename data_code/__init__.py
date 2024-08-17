import pandas as pd


def read_file(string):
    data = pd.read_csv(string)
    return data

def object_datatype():
    data = read_file()
    object_columns = data.select_dtypes(include=['object']).columns
    object_column_names = object_columns.tolist()

    return object_column_names

def isna():
    data = read_file()
    result = data.isna().any().any()
    if result:
        isna_column = data.columns[data.isna().any()].tolist()
        return isna_column
    else:
        return False


def dropna():
    data = read_file()
    if isna():
        data.drop(isna(), axis=1, inplace=True)
    else:
        return False

def data_info():
    data = read_file()
    info = data.info()

    if object_datatype:


    return info

def data_describe():
    data = read_file()
    describe = data.describe()

    return describe

def columns():
    data = read_file()
    columns = data.columns

    return columns

def goupby():
    data = read_file()
    input_columns = input('column name')
    goupby = data.groupby(input_columns).count()

    return goupby


print(object_datatype())