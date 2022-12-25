from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import re
from jarvis import compute as c, speak, record_and_recognize as rr


def reformat(utterance):
    filtered = []
    utterance = re.sub(r'[^\w\s]', " ", utterance.lower())
    words = word_tokenize(utterance)
    for word in words:
        if word not in stopwords.words():
            filtered.append(word)
    return filtered


# Layer 1
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
        return False


def parse_predict():
    lin_reg = ["linear", "regression"]
    k_means = ["clustering"]
    log_reg = ["logistical", "regression"]

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
        return False


def parse_stat_figs():
    avg = ["average"]
    stdev = ["standard", "deviation"]
    median = ["median"]

    speak.ask_stat_figs()
    utterance = rr.record_and_recognize()[0]

    intent = reformat(utterance)
    if avg == intent:
        print("avg")
    elif stdev == intent:
        print("stdev")
    elif median == intent:
        print("median")
    else:
        return False


if __name__ == "__main__":
    parse_func_type()
