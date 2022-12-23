from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import re
import nltk

from jarvis import compute as c, speak


def record():
    pass


def sr():
    """ Recognize recording& return string"""
    pass


def recog_recording():
    return sr(record())


def reformat(utterance):
    filtered = []
    grammar = "NP: {<DT>?<JJ>*<NN>}"
    utterance = re.sub(r'[^\w\s]', " ", utterance.lower())
    words = word_tokenize(utterance)
    for word in words:
        if word not in stopwords.words():
            filtered.append(word)
    nltk.download("averaged_perceptron_tagger")
    filtered_tagged = nltk.pos_tag(filtered)
    chunk_parser = nltk.RegexpParser(grammar)
    intent = chunk_parser.parse(filtered_tagged)
    return intent


# Layer 1
def parse_func_type():
    generate_visualization = ["generate", "visualization"]
    predict = ["predict"]
    calc_stat_figs = ["calculate", "statistical", "key", "figures"]

    speak.ask_func_type()
    utterance = recog_recording()
    intent = reformat(utterance)

    dataset = parse_ds()
    columns, rows = parse_data()

    if generate_visualization in intent:
        parse_vis()
    elif predict in intent:
        parse_predict()
    elif calc_stat_figs in intent:
        parse_predict()
    else:
        return False


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
    utterance = recog_recording()
    intent = reformat(utterance)

    if hist in intent:
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
    utterance = recog_recording()
    intent = reformat(utterance)

    intent = reformat(utterance)
    if lin_reg in intent:
        print("lin_reg")
    elif k_means in intent:
        print("k_means")
    elif log_reg in intent:
        print("log_reg")
    else:
        return False


def parse_stat_figs():
    mean = ["mean"]
    stdev = ["standard", "deviation"]
    median = ["median"]

    speak.ask_stat_figs()
    utterance = recog_recording()
    intent = reformat(utterance)

    intent = reformat(utterance)
    if mean in intent:
        print("mean")
    elif stdev in intent:
        print("stdev")
    elif median in intent:
        print("median")
    else:
        return False
