from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re
import pysnooper
import streamlit as st

from jarvis import speak
from jarvis import record_and_recognize as rr
from jarvis import compute
from jarvis import mongo_query as mq


def reformat(utterance):
    filtered = []
    utterance = re.sub(r'[^\w\s]', " ", utterance.lower())
    words = word_tokenize(utterance)
    for word in words:
        if word not in stopwords.words():
            filtered.append(word)
    return filtered


def greet():
    speak.greet()
    st.write(speak.greeting)


# Layer 1
def parse_func_type():
    generate_visualization = ["generate", "visualization"]
    predict = ["predict"]
    calc_stat_figs = ["calculate", "statistical", "key", "figures"]

    speak.ask_func_type()
    st.write(speak.ques_func_type)
    utterance = rr.record_and_recognize()[0]
    st.write(utterance)
    intent = reformat(utterance)

    if generate_visualization == intent:
        return parse_vis
    elif predict == intent:
        return parse_predict
    elif calc_stat_figs == intent:
        return parse_stat_figs
    else:
        speak.ask_repeat()
        st.write(speak.request_repetition)
        parse_func_type()


# Layer 2
def parse_ds():
    # load list of all datasets
    # Return dataset that corresponds to the user's request
    speak.ask_ds()
    st.write(speak.ques_ds)
    response_df = rr.record_and_recognize()[0].strip()
    st.write(response_df)
    df = mq.load_and_reformat(response_df)
    st.dataframe(df)
    return df


# Layer 3
def parse_data(df):
    # load list & column names into lists
    # parse info on which columns& rows the user wants to use
    # return the rows& columns to be used
    speak.ask_columns()
    st.write(speak.ques_columns)
    response_columns = rr.record_and_recognize()[0].strip()
    st.write(response_columns)
    return response_columns


# Layer 4
def parse_vis(df, column):
    hist = ["histogram"]
    pie = ["pie", "chart"]

    speak.ask_graphs()
    st.write(speak.ques_graphs)
    response_graph = rr.record_and_recognize()[0]
    st.write(response_graph)
    intent = reformat(response_graph)

    if hist == intent:
        compute.plot_histogram(dataframe=df, column=column)
    elif pie == intent:
        return compute.plot_pie_chart(dataframe=df, column=column)
    else:
        speak.ask_repeat()
        parse_vis()


def parse_predict():
    lin_reg = ["linear", "regression"]
    k_means = ["clustering"]
    log_reg = ["logistic", "regression"]

    speak.ask_pred()
    st.write(speak.ques_pred)
    utterance = rr.record_and_recognize()[0]

    intent = reformat(utterance)
    if lin_reg == intent:
        print("lin_reg")
    elif k_means == intent:
        print("k_means")
    elif log_reg == intent:
        print("log_reg")
    else:
        speak.ask_repeat()
        st.write(speak.request_repetition)
        parse_predict()


def parse_stat_figs(df, column):
    avg = ["average"]
    stdev = ["standard", "deviation"]
    median = ["median"]

    speak.ask_stat_figs()
    st.write(speak.ask_stat_figs())
    response_stat_figs = rr.record_and_recognize()[0]
    st.write(response_stat_figs)

    all_figs = compute.composite_stats(dataframe=df, column=column)

    mean_fig = all_figs["mean"]
    median_fig = all_figs["median"]
    mode_fig = all_figs["mode"]
    range_fig = all_figs["range"]
    stdev_fig = all_figs["stddev"]

    intent = reformat(response_stat_figs)
    if avg == intent:
        print(all_figs)
    elif stdev == intent:
        print(all_figs)
    elif median == intent:
        print(all_figs)
    else:
        speak.ask_repeat()
        st.write(speak.request_repetition)
        parse_stat_figs(df, column)


@pysnooper.snoop(depth=3)
def main():
    greet()
    func_type = parse_func_type()
    df = parse_ds()
    column = parse_data(df)
    func_type(df=df, column=column)


if __name__ == "__main__":
    main()
