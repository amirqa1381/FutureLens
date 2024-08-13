import numpy
import pandas as pd


def read_file(string):
    data = pd.read_csv(string)
    return data

# # def drop_na(data):
#
#
# def data_info():
#     data = read_file()
#     info = data.info()
#
#     print(type(data.select_dtypes(include=['object']).columns))
#
#     return info
#
# def data_describe():
#     data = read_file()
#     describe = data.describe()
#
#
#     return describe
#
# def columns():
#     data = read_file()
#     columns = data.columns
#
#     return columns
#
# def goupby():
#     data = read_file()
#     input_columns = input('column name')
#     goupby = data.groupby(input_columns).count()
#
#     return goupby
#
# print(columns())
# print(data_info())