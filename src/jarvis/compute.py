import pandas as pd

FILE_NAME = "customer.csv"
PATH = "/Users/joshua/ws/jarvis/src/jarvis/"


def mean():
    pass


def median():
    pass


def mode():
    pass


def range():
    pass


def standard_deviation():
    pass


def plot_histogram():
    pass


def plot_scatter_plot():
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
    load_data()
