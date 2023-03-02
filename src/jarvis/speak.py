from gtts import gTTS
from playsound import playsound

greeting = "Hello, nice to meet you! I'm Jarvis"

ques_func_type = \
    "How may I help you today? Would you like to Calculate statistical key figures," \
    " generate a visualization or predict?"

ques_ds = "Which data set should I use?"

ques_columns = "Which columns would you like to use?"

request_repetition = "I'm not sure I understand. Could you repeat please?"

ques_graphs = "What type of graph would you like me to create? A pie chart, or a histogram?"

ques_pred = \
    "Which prediction algorithm should I use? Linear regression, logistic regression or k-means clustering?"

ques_stat_figs = "Which statistical figures should I calculate? The mean, the median or the standard deviation?"

error_df_not_found = "Sorry, but I wasn't able to find the dataset you requested"

error_column_not_found = "Sorry, but I wasn't able to find the column you requested"

ques_algo = "What is the name of the model you would like to use?"

ques_mlds = "Which dataset would you like to perform the prediction on?"


def generate_greeting(ques):
    tts = gTTS(ques)
    tts.save("/Users/joshua/ws/jarvis/src/jarvis/voices/greeting.mp3")


def generate_ques_func_type(ques):
    tts = gTTS(ques)
    tts.save("/Users/joshua/ws/jarvis/src/jarvis/voices/ques_func_type.mp3")


def generate_ques_ds(ques):
    tts = gTTS(ques)
    tts.save("/Users/joshua/ws/jarvis/src/jarvis/voices/ques_ds.mp3")


def generate_ques_columns(ques):
    tts = gTTS(ques)
    tts.save("/Users/joshua/ws/jarvis/src/jarvis/voices/ques_columns.mp3")


def generate_repetition_request(ques):
    tts = gTTS(ques)
    tts.save("/Users/joshua/ws/jarvis/src/jarvis/voices/request_repetition.mp3")


def generate_graph_ques(ques):
    tts = gTTS(ques)
    tts.save("/Users/joshua/ws/jarvis/src/jarvis/voices/ques_graphs.mp3")


def generate_predict_ques(ques):
    tts = gTTS(ques)
    tts.save("/Users/joshua/ws/jarvis/src/jarvis/voices/ques_pred.mp3")


def generate_stat_ques(ques):
    tts = gTTS(ques)
    tts.save("/Users/joshua/ws/jarvis/src/jarvis/voices/ques_stat_figs.mp3")


def generate_error_df_not_found(ques):
    tts = gTTS(ques)
    tts.save("/Users/joshua/ws/jarvis/src/jarvis/voices/error_df_not_found.mp3")


def generate_error_column_not_found(ques):
    tts = gTTS(ques)
    tts.save("/Users/joshua/ws/jarvis/src/jarvis/voices/error_column_not_found.mp3")


def generate_ques_algo(ques):
    tts = gTTS(ques)
    tts.save("/Users/joshua/ws/jarvis/src/jarvis/voices/ques_algo.mp3")


def generate_all_files():
    generate_greeting(greeting)
    generate_ques_func_type(ques_func_type)
    generate_ques_ds(ques_ds)
    generate_ques_columns(ques_columns)
    generate_repetition_request(request_repetition)
    generate_graph_ques(ques_graphs)
    generate_predict_ques(ques_pred)
    generate_stat_ques(ques_stat_figs)


def greet():
    playsound("/Users/joshua/ws/jarvis/src/jarvis/voices/greeting.mp3")


def ask_func_type():
    playsound("/Users/joshua/ws/jarvis/src/jarvis/voices/ques_func_type.mp3")


def ask_ds():
    playsound("/Users/joshua/ws/jarvis/src/jarvis/voices//ques_ds.mp3")


def ask_columns():
    playsound("/Users/joshua/ws/jarvis/src/jarvis/voices/ques_columns.mp3")


def ask_repeat():
    playsound("/Users/joshua/ws/jarvis/src/jarvis/voices/request_repetition.mp3")


def ask_graphs():
    playsound("/Users/joshua/ws/jarvis/src/jarvis/voices/ques_graphs.mp3")


def ask_pred():
    playsound("/Users/joshua/ws/jarvis/src/jarvis/voices/ques_pred.mp3")


def ask_stat_figs():
    playsound("/Users/joshua/ws/jarvis/src/jarvis/voices/ques_stat_figs.mp3")


def say_error_df_not_found():
    playsound("/Users/joshua/ws/jarvis/src/jarvis/voices/error_df_not_found.mp3")


def say_error_column_not_found():
    playsound("/Users/joshua/ws/jarvis/src/jarvis/voices/error_column_not_found.mp3")


def ask_algo():
    playsound("/Users/joshua/ws/jarvis/src/jarvis/voices/ques_algo.mp3")


def ask_all_ques():
    greet()
    ask_func_type()
    ask_ds()
    ask_columns()
    ask_repeat()
    ask_graphs()
    ask_pred()
    ask_stat_figs()


if __name__ == "__main__":
    generate_ques_algo(ques_algo)
    ask_algo()
