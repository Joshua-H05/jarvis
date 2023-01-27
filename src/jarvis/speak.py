from gtts import gTTS
from playsound import playsound


def generate_files():
    greeting = "Hello! Jarvis at your service"
    tts1 = gTTS(greeting)
    tts1.save("/Users/joshua/ws/jarvis/src/jarvis/greeting.mp3")

    ques_func_type = \
        "What would you like to do? Calculate statistical key figures, generate a visualization or predict?"
    tts2 = gTTS(ques_func_type)
    tts2.save("/Users/joshua/ws/jarvis/src/jarvis/ques_func_type.mp3")

    ques_func = "What exactly would you like me to calculate?"
    tts3 = gTTS(ques_func)
    tts3.save("/Users/joshua/ws/jarvis/src/jarvis/ques_func.mp3")

    ques_ds = "Which data set should I use?"
    tts4 = gTTS(ques_ds)
    tts4.save("/Users/joshua/ws/jarvis/src/jarvis/ques_ds.mp3")

    ques_rows = "Which rows should I use?"
    tts5 = gTTS(ques_rows)
    tts5.save("ques_rows.mp3")

    ques_columns = "Which columns should I use?"
    tts6 = gTTS(ques_columns)
    tts6.save("ques_columns.mp3")

    request_repetition = "I'm not sure I understand. Could you repeat please?"
    tts7 = gTTS(request_repetition)
    tts7.save("/Users/joshua/ws/jarvis/src/jarvis/request_repetition.mp3")

    understand = "I'm on it!"
    tts8 = gTTS(understand)
    tts8.save("understand.mp3")

    ques_df = "Which dataframe should I use?"
    tts9 = gTTS(ques_df)
    tts9.save("/Users/joshua/ws/jarvis/src/jarvis/voices/ques_df.mp3")

    # Graphs
    ques_graphs = "What type of graph would you like me to create? A pie chart, or a histogram?"
    tts10 = gTTS(ques_graphs)
    tts10.save("ques_graphs.mp3")

    # Predict
    ques_pred = \
        "Which prediction algorithm should I use? Linear regression, logistic regression or k-means clustering?"
    tts11 = gTTS(ques_pred)
    tts11.save("ques_pred.mp3")

    # Statistical key figures
    ques_stat_figs = "Which statistical figures should I calculate? The mean, the median or the standard deviation?"
    tts12 = gTTS(ques_stat_figs)
    tts12.save("ques_stat_figs.mp3")


def greet():
    playsound("/Users/joshua/ws/jarvis/src/jarvis/voices/greeting.mp3")
    return False


def ask_func_type():
    playsound("/Users/joshua/ws/jarvis/src/jarvis/voices/ques_func_type.mp3")


def ask_func():
    playsound("/Users/joshua/ws/jarvis/src/jarvis/voices/ques_func.mp3")


def ask_ds():
    playsound("/Users/joshua/ws/jarvis/src/jarvis/voices/ques_ds.mp3")


def ask_repeat():
    playsound("/Users/joshua/ws/jarvis/src/jarvis/voices/request_repetition.mp3")


def understand():
    playsound("/Users/joshua/ws/jarvis/src/jarvis/voices/understand.mp3")


def ask_rows():
    playsound("/Users/joshua/ws/jarvis/src/jarvis/voices/ques_rows.mp3")


def ask_columns():
    playsound("/Users/joshua/ws/jarvis/src/jarvis/voices/ques_columns.mp3")


def ask_dataframe():
    playsound("/Users/joshua/ws/jarvis/src/jarvis/voices/ques_ds.mp3")


def ask_graphs():
    playsound("/Users/joshua/ws/jarvis/src/jarvis/voices/ques_graphs.mp3")


def ask_pred():
    playsound("/Users/joshua/ws/jarvis/src/jarvis/voices/ques_pred.mp3")


def ask_stat_figs():
    playsound("/Users/joshua/ws/jarvis/src/jarvis/voices/ques_stat_figs.mp3")


if __name__ == "__main__":
    ask_dataframe()
    ask_columns()
    """ask_rows()
    ask_columns()
    ask_graphs()
    ask_pred()
    ask_stat_figs()"""
