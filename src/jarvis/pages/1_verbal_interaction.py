from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re
import pysnooper
import streamlit as st

from jarvis import speak, mongo_query as mq, record_and_recognize as rr, compute, ml


def reformat(utterance):
    filtered = []
    utterance = re.sub(r'[^\w\s]', " ", utterance.lower())
    words = word_tokenize(utterance)
    for word in words:
        if word not in stopwords.words():
            filtered.append(word)
    return filtered


def greet():
    st.write(speak.greeting)
    speak.greet()


# Layer 1
def ask_func_type():
    if st.session_state["run"]:
        st.write(speak.ques_func_type)
        speak.ask_func_type()
        utterance = rr.record_and_recognize()["text"]
        st.write(utterance)
        intent = reformat(utterance)
        return intent


def parse_func_type():
    generate_visualization = ["generate", "visualization"]
    predict = ["predict"]
    calc_stat_figs = ["calculate", "statistical", "key", "figures"]

    if st.session_state["run"]:
        while True:
            intent = ask_func_type()
            if generate_visualization == intent:
                return "vis"
            elif predict == intent:
                return "pred"
            elif calc_stat_figs == intent:
                return "figs"
            else:
                speak.ask_repeat()
                st.write(speak.request_repetition)


# Layer 2
def ask_ds():
    if st.session_state["run"]:
        st.write(speak.ques_ds)
        speak.ask_ds()
        response_df = rr.record_and_recognize()["text"]
        st.write(response_df)
        return response_df


def ask_mlds():
    if st.session_state["run"]:
        st.write(speak.ques_mlds)
        speak.ask_pred_data()
        data = rr.record_and_recognize()["text"]
        st.write(data)
        return data


def ask_model():
    if st.session_state["run"]:
        st.write(speak.ques_algo)
        speak.ask_algo()
        response_df = rr.record_and_recognize()["text"]
        st.write(response_df)
        return response_df


def verify_mlds():
    collections = mq.list_all_collections()
    if st.session_state["run"]:
        while True:
            response_df = ask_mlds()
            if response_df in collections:
                df = mq.load_and_reformat(response_df)
                st.dataframe(df)
                return df
            else:
                st.write(speak.error_df_not_found)
                speak.say_error_df_not_found()


def verify_ds():
    # load list of all datasets
    # Return dataset that corresponds to the user's request

    collections = mq.list_all_collections()
    if st.session_state["run"]:
        while True:
            response_df = ask_ds()
            if response_df in collections:
                df = mq.load_and_reformat(response_df)
                st.dataframe(df)
                return df
            else:
                st.write(speak.error_df_not_found)
                speak.say_error_df_not_found()


# Layer 3
def ask_data():
    if st.session_state["run"]:
        st.write(speak.ques_columns)
        speak.ask_columns()
        response_columns = rr.record_and_recognize()["text"].strip()
        st.write(response_columns)
        return response_columns


def parse_data(df):
    # load list & column names into lists
    # parse info on which columns& rows the user wants to use
    # return the rows& columns to be used
    columns = mq.list_all_columns(df)
    if st.session_state["run"]:
        while True:
            response_columns = ask_data()
            if response_columns in columns:
                return response_columns
            else:
                st.write(speak.error_column_not_found)
                speak.say_error_column_not_found()


# Layer 4
def parse_vis(df, column):
    hist = ["histogram"]
    pie = ["pie", "chart"]

    if st.session_state["run"]:
        st.write(speak.ques_graphs)
        speak.ask_graphs()
        response_graph = rr.record_and_recognize()["text"]
        st.write(response_graph)
        intent = reformat(response_graph)

        if hist == intent:
            compute.plot_histogram(dataframe=df, column=column)
        elif pie == intent:
            return compute.plot_pie_chart(dataframe=df, column=column)
        else:
            speak.ask_repeat()
            parse_vis(df, column)


def ask_predict():
    if st.session_state["run"]:
        st.write(speak.ques_algo)
        speak.ask_algo()
        utterance = rr.record_and_recognize()["text"]
        st.write(utterance)
        return utterance


def parse_predict():
    lin_reg = ["linear", "regression"]
    log_reg = ["logistic", "regression"]

    if st.session_state["run"]:
        while True:
            utterance = ask_predict()
            intent = reformat(utterance)
            if lin_reg == intent:
                print("lin_reg")
            elif log_reg == intent:
                print("log_reg")
            else:
                st.write(speak.request_repetition)
                speak.ask_repeat()


def ask_stat_figs():
    if st.session_state["run"]:
        st.write(speak.ques_stat_figs)
        speak.ask_stat_figs()
        response_stat_figs = rr.record_and_recognize()["text"]
        st.write(response_stat_figs)
        intent = reformat(response_stat_figs)
        return intent


@pysnooper.snoop(depth=2)
def parse_stat_figs(df, column):
    avg = ["average"]
    stdev = ["standard", "deviation"]
    median = ["median"]

    all_figs = compute.composite_stats(dataframe=df, column=column)

    mean_fig = all_figs["mean"]
    median_fig = all_figs["median"]
    mode_fig = all_figs["mode"]
    range_fig = all_figs["range"]
    stdev_fig = all_figs["stddev"]

    if st.session_state["run"]:
        while True:
            intent = ask_stat_figs()
            if avg == intent:
                st.write(str(mean_fig))
                break
            elif stdev == intent:
                st.write(str(stdev_fig))
                break
            elif median == intent:
                st.write(str(median_fig))
                break
            else:
                speak.ask_repeat()
                st.write(speak.request_repetition)


def info():
    df = verify_ds()
    column = parse_data(df)
    return df, column


def parse_model():
    collections = ml.list_all_models()
    if st.session_state["run"]:
        while True:
            response = ask_model()
            if response in collections:
                return response
            else:
                st.write(speak.error_df_not_found)
                speak.say_error_df_not_found()


@pysnooper.snoop()
def verbal_interaction():
    st.session_state["run"] = False

    st.sidebar.write("# Here are the available datasets:")
    for item in mq.list_all_collections():
        st.sidebar.write("- " + item)
    st.header("Jarvis, your data analysis assistant!")
    start, stop = st.columns(2)
    if start.button("Click to start!"):
        st.session_state["run"] = True

    if stop.button("Click to stop"):
        st.session_state["run"] = False

    while st.session_state["run"]:
        greet()
        func_type = parse_func_type()
        if func_type == "pred":
            model = parse_model()
            ds = verify_mlds()
            results = ml.predict_stored_model(model_name=model, df=ds)
            st.dataframe(results)

        if func_type == "vis":
            df, column = info()
            parse_vis(df, column)

        elif func_type == "figs":
            df, column = info()
            parse_stat_figs(df,column)



if __name__ == "__main__":
    verbal_interaction()
