# Citation complete

import pandas as pd
import pysnooper

def replace_nan_with_zeros_in_column(input_df, column_name):
    # Create a copy of the input DataFrame to avoid modifying the original DataFrame
    df_with_zeros = input_df.copy()
    df_with_zeros[column_name] = df_with_zeros[column_name].fillna(0)
    return df_with_zeros

@pysnooper.snoop()
def replace(df, column, method):
    if method == "drop":
        df_without_missing = df.dropna(axis=1)
        return df_without_missing
    elif method == "zero":
        return replace_nan_with_zeros_in_column(df, column)
    elif method == "mean":
        mean = df[column].mean()
        df[column] = df[column].fillna(mean)
        return df
    elif method == "median":
        median = df[column].median()
        df[column] = df[column].fillna(median)
        return df


# Hands on machine learning with scikit learn and tensor flow pg. 60


def one_hot(df, column):
    encoded = pd.get_dummies(data=df, columns=[column])
    return encoded

# Source: https://towardsdatascience.com/one-hot-encoding-scikit-vs-pandas-2133775567b8 4th April


def rm_col(df, *args):
    for col in args:
        df = df.drop(col, axis=1)
    return df


# Source: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop.html 4th April

def rm_row(df, *args):
    for row in args:
        df = df.drop(row, axis=0)
    df = df.reset_index(drop=True)
    return df


def operation(df, name, operator, col1, col2):
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

# Source: https://thispointer.com/pandas-add-two-columns-into-a-new-column-in-dataframe/ 4th April
