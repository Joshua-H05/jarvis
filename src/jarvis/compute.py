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
    fig = px.histogram(dataframe, x=column)
    st.plotly_chart(fig)


def plot_scatter_plot(df, x_var, y_var):
    fig = px.scatter(df, x_var, y_var)
    fig.show()


def plot_pie_chart(dataframe, column):
    fig = px.pie(dataframe, names=column, color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(fig)


if __name__ == "__main__":
    df = mq.load_and_reformat("cars")
    plot_scatter_plot(df, "age", "salary")
