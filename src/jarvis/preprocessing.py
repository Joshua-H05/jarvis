import pandas as pd
import pysnooper


def normalize(df):
    pass


def replace(df, column, method):
    if method == "drop":
        df[column].dropna()
    elif method == "zero":
        df[column].fillna(0)
    elif method == "mean":
        mean = df[column].mean()
        df[column].fillna(mean)
    elif method == "median":
        median = df[column].median()
        df[column].fillna(median)
    return df

# Hands on machine learning with scikit learn and tensor flow pg. 60


def one_hot(df, column):
    encoded = pd.get_dummies(data=df, columns=[column])
    return encoded

# https://towardsdatascience.com/one-hot-encoding-scikit-vs-pandas-2133775567b8 4th April


def rm_col(df, *args):
    for col in args:
        df = df.drop(col, axis=1)
    return df


# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop.html 4th April

def rm_row(df, *args):
    for row in args:
        df = df.drop(row, axis=0)
    df = df.reset_index(drop=True)
    return df


def operation(df, name, operator, col1, col2):
    print(type(df[col1]))
    first = df[col1].astype("float32")
    second = df[col2].astype("float32")
    if operator == "+":
        df[name] = first + second
    elif operator == "-":
        df[name] = first - second
    elif operator == "*":
        df[name] = first * second
    elif operator == "/":
        df[name] = first / second

    return df

# https://thispointer.com/pandas-add-two-columns-into-a-new-column-in-dataframe/ 4th April
