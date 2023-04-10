from gtts import gTTS
from playsound import playsound
import pathlib


DIR = pathlib.Path.cwd() / "src/jarvis/voices/"


utterances = {"greeting": ["Hello, nice to meet you! I'm Jarvis",
                           "/Users/joshua/ws/jarvis/src/jarvis/voices/greeting.mp3"],

              "func_type": ["How may I help you today? Would you like to Calculate statistical key figures,"
                            " generate a visualization or predict?",
                            "/Users/joshua/ws/jarvis/src/jarvis/voices/func_type.mp3"],

              "ques_ds": ["Which data set should I use?", "/Users/joshua/ws/jarvis/src/jarvis/voices/ques_ds.mp3"],

              "ques_columns": ["Which columns would you like to use?",
                               "/Users/joshua/ws/jarvis/src/jarvis/voices/ques_columns.mp3"],

              "request_repetition": ["I'm not sure I understand. Could you repeat please?",
                                     "/Users/joshua/ws/jarvis/src/jarvis/voices/request_repetition.mp3"],

              "ques_graphs": ["What type of graph would you like me to create? A pie chart, or a histogram?",
                              "/Users/joshua/ws/jarvis/src/jarvis/voices/ques_graphs.mp3"],

              "ques_pred": ["Which prediction algorithm should I use? Linear regression, "
                            "logistic regression or k-means clustering?",
                            "/Users/joshua/ws/jarvis/src/jarvis/voices/ques_pred.mp3"],

              "ques_stat_figs": ["Which statistical figures should I calculate? The mean, the median or the standard "
                                 "deviation?", "/Users/joshua/ws/jarvis/src/jarvis/voices/ques_stat_figs.mp3"],

              "error_df_not_found": ["Sorry, but I wasn't able to find the dataset you requested",
                                     "/Users/joshua/ws/jarvis/src/jarvis/voices/error_df_not_found.mp3"],

              "error_column_not_found": ["Sorry, but I wasn't able to find the column you requested",
                                         "/Users/joshua/ws/jarvis/src/jarvis/voices/error_column_not_found.mp3"],

              "ques_algo": ["What is the name of the model you would like to use?",
                            "/Users/joshua/ws/jarvis/src/jarvis/voices/ques_algo.mp3"],
              "ques_mlds": ["Which dataset would you like to perform the prediction on?",
                            "/Users/joshua/ws/jarvis/src/jarvis/voices/ques_pred_data.mp3"]
              }


def generate_all_files():
    for utterance in utterances.values():
        tts = gTTS(utterance[0])
        tts.save(utterance[1])


def say(utterance):
    path = utterances[utterance][1]
    playsound(path)


if __name__ == "__main__":
    generate_all_files()
    say("greeting")
