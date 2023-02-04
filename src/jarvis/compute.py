import seaborn as sns
import matplotlib.pyplot as plt
from jarvis import mongo_query as mq
import streamlit as st


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


def plot_histogram(dataframe, column):
    sns.displot(dataframe[column].astype("float"))
    st.pyplot()


def plot_scatter_plot(dataframe, x_var, y_var, binary_class=None):
    pass


def plot_pie_chart(dataframe, column):
    groups = dataframe[column].unique().tolist()
    groups.sort()
    values = dataframe[column].tolist()
    nums = []
    for group in groups:
        nums.append(values.count(group))
    plt.pie(nums, labels=None, autopct='%1.1f%%')
    plt.legend(labels=groups, loc=1)
    st.pyplot()


if __name__ == "__main__":
    df = mq.load_and_reformat("cars")
    plot_pie_chart(df, "gender")
    plot_histogram(df, "salary")
