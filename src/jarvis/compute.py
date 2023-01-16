import pandas as pd
from jarvis import mongo_query as mq


FILE_NAME = "customer.csv"
PATH = "/Users/joshua/ws/jarvis/src/jarvis/"


def compute_mean(dataframe, column):
    avg = dataframe[column].astype(int).mean()
    return avg


def compute_median(dataframe, column):
    med = dataframe[column].astype(int).median()
    return med


def compute_mode(dataframe, column):
    mode = dataframe[column].astype(int).mode(dropna=True).tolist()
    return mode


def compute_range(dataframe, column):
    greatest = int(dataframe[column].astype(int).nlargest(n=1))
    smallest = int(dataframe[column].astype(int).nsmallest(n=1))
    dif = greatest - smallest
    return dif


def standard_deviation(dataframe, column):
    stddev = dataframe[column].astype(int).std()
    return stddev


def plot_histogram():
    pass


def plot_scatter_plot(df, x_var, y_var, binary_class=None):
    pass


def plot_pie_chart():
    pass


def load_data():
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', -1)
    customers = pd.read_csv(f"{PATH}{FILE_NAME}")
    print(str(customers))


if __name__ == "__main__":
    df = mq.load_and_reformat("suv_sales")
    avg = compute_mean(df, "Age")
    med = compute_median(df, "Age")
    mode = compute_mode(df, "Age")
    r = compute_range(df, "Age")
    stddev = standard_deviation(df, "Age")
    print(mode)
