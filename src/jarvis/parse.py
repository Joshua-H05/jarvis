from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import re
import pysnooper

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


# Layer 1
@pysnooper.snoop(depth=3)
def parse_func_type():
    generate_visualization = ["generate", "visualization"]
    predict = ["predict"]
    calc_stat_figs = ["calculate", "statistical", "key", "figures"]

    speak.ask_func_type()
    utterance = rr.record_and_recognize()[0]
    print(utterance)
    intent = reformat(utterance)

    """dataset = parse_ds()
    columns, rows = parse_data()"""

    if generate_visualization == intent:
        parse_vis()
    elif predict == intent:
        parse_predict()
    elif calc_stat_figs == intent:
        parse_stat_figs()
    else:
        speak.ask_repeat()
        parse_func_type()


# Layer 2
def parse_ds():
    pass
    # load list of all datasets
    # Return dataset that corresponds to the user's request


# Layer 3
def parse_data():
    pass
    # load list & column names into lists
    # parse info on which columns& rows the user wants to use
    # return the rows& columns to be used


# Layer 4
def parse_vis():
    hist = ["histogram"]
    pie = ["pie", "chart"]

    speak.ask_graphs()
    utterance = rr.record_and_recognize()[0]
    intent = reformat(utterance)

    if hist == intent:
        print("hist")
    elif pie in intent:
        print("pie")
    else:
        speak.ask_repeat()
        parse_vis()


def parse_predict():
    lin_reg = ["linear", "regression"]
    k_means = ["clustering"]
    log_reg = ["logistic", "regression"]

    speak.ask_pred()
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
        parse_predict()


@pysnooper.snoop(depth=2)
def parse_stat_figs():  # currently missing df and column
    avg = ["average"]
    stdev = ["standard", "deviation"]
    median = ["median"]

    speak.ask_dataframe()
    response_df = reformat(rr.record_and_recognize()[0])[0]
    df = mq.load_and_reformat(response_df)
    print(df)

    speak.ask_columns()
    response_columns = reformat(rr.record_and_recognize()[0])[0]

    speak.ask_stat_figs()
    response_stat_figs = rr.record_and_recognize()[0]

    all_figs = compute.composite_stats(dataframe=df, column=response_columns)

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
        parse_stat_figs()


if __name__ == "__main__":
    greet()
    parse_func_type()
