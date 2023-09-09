# All functions followed by "st." leverage streamlit. The sole source consulted was the official documentation
# provided by Streamlit: https://docs.streamlit.io

import os
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re
import streamlit as st
from streamlit_chat import message

from jarvis import speak, mongo_query as mq, record_and_recognize as rr, compute, ml

KEY = 0


def reformat(utterance):
    filtered = []
    utterance = re.sub(r'[^\w\s]', " ", utterance.lower())
    words = word_tokenize(utterance)
    for word in words:
        if word not in stopwords.words():
            filtered.append(word)
    return filtered


def greet():
    message(speak.utterances["greeting"][0])
    speak.say("greeting")


# Layer 1
def ask_func_type():
    if st.session_state["run"]:
        while True:
            global KEY
            KEY += 1
            message(speak.utterances["func_type"][0], key=str(KEY))
            speak.say("func_type")
            transcription = rr.record_and_recognize()
            if transcription:
                utterance = transcription["text"]
                KEY += 1
                message(utterance, is_user=True, key=str(KEY))
                intent = reformat(utterance)
                return intent
            else:
                KEY += 1
                message(speak.utterances["request_repetition"][0], key=str(KEY))
                speak.say("request_repetition")


def parse_func_type():
    generate_visualization = ["generate", "visualization"]
    predict = ["predict"]
    calc_stat_figs = ["calculate", "statistical", "key", "figures"]

    if st.session_state["run"]:
        greet()
        while True:
            intent = ask_func_type()
            if generate_visualization == intent:
                return "vis"
            elif predict == intent:
                return "pred"
            elif calc_stat_figs == intent:
                return "figs"
            else:
                global KEY
                KEY += 1
                speak.say("request_repetition")
                message(speak.utterances["request_repetition"][0], key=str(KEY))


# Layer 2
def ask_ds():
    if st.session_state["run"]:
        while True:
            global KEY
            KEY += 1
            message(speak.utterances["ques_ds"][0], key=str(KEY))
            speak.say("ques_ds")
            response_df = rr.record_and_recognize()
            if response_df:
                utterance = response_df["text"]
                KEY += 1
                message(utterance, is_user=True, key=str(KEY))
                return utterance
            else:
                KEY += 1
                message(speak.utterances["request_repetition"][0], key=str(KEY))
                speak.say("request_repetition")


def ask_mlds():
    if st.session_state["run"]:
        while True:
            global KEY
            KEY += 1
            message(speak.utterances["ques_mlds"][0], key=str(KEY))
            speak.say("ques_mlds")
            data = rr.record_and_recognize()
            if data:
                utterance = data["text"]
                KEY += 1
                message(utterance, is_user=True, key=str(KEY))
                return utterance
            else:
                KEY += 1
                message(speak.utterances["request_repetition"][0], key=str(KEY))
                speak.say("request_repetition")


def ask_model():
    if st.session_state["run"]:
        while True:
            global KEY
            KEY += 1
            message(speak.utterances["ques_algo"][0], key=str(KEY))
            speak.say("ques_algo")
            response_df = rr.record_and_recognize()
            if response_df:
                utterance = response_df["text"]
                KEY += 1
                message(utterance, is_user=True, key=str(KEY))
                return utterance
            else:
                KEY += 1
                message(speak.utterances["request_repetition"][0], key=str(KEY))
                speak.say("request_repetition")


def verify_mlds():
    collections = mq.list_all_collections()
    if st.session_state["run"]:
        while True:
            response_df = ask_mlds()
            if response_df in collections:
                df = mq.load_and_reformat(response_df)
                return df
            else:
                global KEY
                KEY += 1
                message(speak.utterances["error_df_not_found"][0], key=str(KEY))
                speak.say("error_df_not_found")


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
                global KEY
                KEY += 1
                message(speak.utterances["error_df_not_found"][0], key=str(KEY))
                speak.say("error_df_not_found")


# Layer 3
def ask_data():
    if st.session_state["run"]:
        while True:
            global KEY
            KEY += 1
            message(speak.utterances["ques_columns"][0], key=str(KEY))
            speak.say("ques_columns")
            response_columns = rr.record_and_recognize()
            if response_columns:
                utterance = response_columns["text"].strip()
                KEY += 1
                message(utterance, is_user=True, key=str(KEY))
                return utterance
            else:
                KEY += 1
                message(speak.utterances["request_repetition"][0], key=str(KEY))
                speak.say("request_repetition")


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
                global KEY
                KEY += 1
                message(speak.utterances["error_column_not_found"][0], key=str(KEY))
                speak.say("error_column_not_found")


# Layer 4
def parse_vis(df, column):
    hist = ["histogram"]
    pie = ["pie", "chart"]

    if st.session_state["run"]:
        while True:
            global KEY
            KEY += 1
            message(speak.utterances["ques_graphs"][0], key=str(KEY))
            speak.say("ques_graphs")
            response_graph = rr.record_and_recognize()
            if response_graph:
                utterance = response_graph["text"]
                KEY += 1
                message(utterance, is_user=True, key=str(KEY))
                intent = reformat(utterance)

                if hist == intent:
                    return compute.plot_histogram(dataframe=df, column=column)
                elif pie == intent:
                    return compute.plot_pie_chart(dataframe=df, column=column)
                else:
                    KEY += 1
                    speak.say("request_repetition")
                    message(speak.utterances["request_repetition"][0], key=str(KEY))
                    parse_vis(df, column)
            else:
                KEY += 1
                message(speak.utterances["request_repetition"][0], key=str(KEY))
                speak.say("request_repetition")


def ask_predict():
    if st.session_state["run"]:
        global KEY
        KEY += 1
        message(speak.utterances["ques_algo"][0], key=str(KEY))
        speak.say("ques_algo")
        utterance = rr.record_and_recognize()["text"]
        KEY += 1
        message(utterance, is_user=True, key=str(KEY))
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
                global KEY
                KEY += 1
                speak.say("request_repetition")
                message(speak.utterances["request_repetition"][0], key=str(KEY))


def ask_stat_figs():
    if st.session_state["run"]:
        while True:
            global KEY
            KEY += 1
            message(speak.utterances["ques_stat_figs"][0], key=str(KEY))
            speak.say("ques_stat_figs")
            response_stat_figs = rr.record_and_recognize()
            if response_stat_figs:
                utterance = response_stat_figs["text"]
                KEY += 1
                message(utterance, is_user=True, key=str(KEY))
                intent = reformat(utterance)
                return intent
            else:
                KEY += 1
                message(speak.utterances["request_repetition"][0], key=str(KEY))
                speak.say("request_repetition")


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
                global KEY
                KEY += 1
                speak.say("request_repetition")
                message(speak.utterances["request_repetition"][0], key=str(KEY))


def info():
    if st.session_state["run"]:
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
                global KEY
                KEY += 1
                message(speak.utterances["model_not_found"][0], key=str(KEY))
                speak.say("model_not_found")


def verbal_interaction():
    st.session_state["run"] = False

    st.sidebar.write("# Here are the available datasets:")
    for item in mq.list_all_collections():
        st.sidebar.write("- " + item)

    st.sidebar.write("# Here are the available models:")
    for item in ml.list_all_models():
        st.sidebar.write("- " + item)

    st.header("Jarvis, your data analysis assistant!")
    start, stop = st.columns(2)

    if start.button("Click to start!"):
        st.session_state["run"] = True

    if stop.button("Click to stop"):
        st.session_state["run"] = False

    while st.session_state["run"]:
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
            parse_stat_figs(df, column)

        st.session_state["run"] = False


if __name__ == "__main__":
    verbal_interaction()
