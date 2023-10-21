# Citation complete
from jarvis import mongo_query as mq
import streamlit as st
import plotly.express as px

def composite_stats(dataframe, column):

    statistics = {
        "mean": compute_mean,
        "median": compute_median,
        "mode": compute_mode,
        "range": compute_range,
        "stddev": standard_deviation,
    }

    stat_results = {}
    for stat_name, calculation in statistics.items():
        stat_results[stat_name] = calculation(dataframe, column)

    return stat_results


def compute_mean(dataframe, column):
    avg = dataframe[column].astype(int).mean()
    return avg
# Derived from source: https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html
# Date last accessed: Jan 27 2023

def compute_median(dataframe, column):
    med = dataframe[column].astype(int).median()
    return med
# Derived from source: https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html
# Date last accessed: Jan 27 2023


def compute_mode(dataframe, column):
    mode = dataframe[column].astype(int).mode(dropna=True).tolist()
    if len(mode) == 1:
        return mode[0]
    else:
        return mode
# Derived from source: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mode.html
# Date last accessed: Jan 27 2023

def compute_range(dataframe, column):
    greatest = int(dataframe[column].astype(int).nlargest(n=1))
    smallest = int(dataframe[column].astype(int).nsmallest(n=1))
    dif = greatest - smallest
    return dif


def standard_deviation(dataframe, column):
    stddev = dataframe[column].astype(int).std()
    return stddev
# Derived from source: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.std.html
# Date last accessed: 29. August 2023

def plot_histogram(dataframe, column, st_col=None):
    fig = px.histogram(dataframe, x=column)
    st.plotly_chart(fig)
# Derived from source: https://plotly.com/python/histograms/
# Date last accessed: Feb 12, 2023


def plot_scatter_plot(df, x_var, y_var, st_col=None):
    fig = px.scatter(df, x_var, y_var)
    st.plotly_chart(fig)
# Derived from source: https://plotly.com/python/line-and-scatter/
# Date last accessed: Feb 12, 2023


def plot_pie_chart(dataframe, column, st_col=None):
    fig = px.pie(dataframe, names=column, color_discrete_sequence=px.colors.sequential.Blues)
    st.plotly_chart(fig)
# Derived from source: https://plotly.com/python/pie-charts/
# Date last accessed: Feb 12, 2023


def plot_bar_chart(dataframe, x, y, st_col=None):
    fig = px.bar(dataframe, x=x, y=y)
    st.plotly_chart(fig)
# Derived from source: https://plotly.com/python/bar-charts/
# Date last accessed: Jul 15, 2023



if __name__ == "__main__":
    df = mq.load_and_reformat("cars")
    plot_scatter_plot(df, "age", "salary")
