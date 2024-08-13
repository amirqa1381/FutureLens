import pandas as pd


def read_file():
    data = pd.read_csv(r"C:\Users\ae_sa\OneDrive\Desktop\data scientist\data analysis\data sets\Iris.csv")
    return data.head()
