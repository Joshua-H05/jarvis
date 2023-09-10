# Citation complete
from gtts import gTTS
import os


CWD = os.getcwd()
MEDIADIR = f"{CWD}/src/jarvis"

utterances = {"greeting": ["Hello, nice to meet you! I'm Jarvis",
                           f"{MEDIADIR}/greeting.mp3"],

              "func_type": ["How may I help you today? Would you like to Calculate statistical key figures,"
                            " generate a visualization or predict?",
                            f"{MEDIADIR}/func_type.mp3"],

              "ques_ds": ["Which data set should I use?", f"/{MEDIADIR}/ques_ds.mp3"],

              "ques_columns": ["Which columns would you like to use?",
                               f"{MEDIADIR}/ques_columns.mp3"],

              "request_repetition": ["I'm not sure I understand. Could you repeat please?",
                                     f"{MEDIADIR}/request_repetition.mp3"],

              "ques_graphs": ["What type of graph would you like me to create? A pie chart, or a histogram?",
                              f"{MEDIADIR}/ques_graphs.mp3"],

              "ques_pred": ["Which prediction algorithm should I use? Linear regression, "
                            "logistic regression or k-means clustering?",
                            f"{MEDIADIR}/ques_pred.mp3"],

              "ques_stat_figs": ["Which statistical figures should I calculate? The mean, the median or the standard "
                                 "deviation?", f"{MEDIADIR}/ques_stat_figs.mp3"],

              "error_df_not_found": ["Sorry, but I wasn't able to find the dataset you requested",
                                     f"{MEDIADIR}/error_df_not_found.mp3"],

              "error_column_not_found": ["Sorry, but I wasn't able to find the column you requested",
                                         f"{MEDIADIR}/error_column_not_found.mp3"],

              "ques_algo": ["What is the name of the model you would like to use?",
                            f"{MEDIADIR}/ques_algo.mp3"],
              "ques_mlds": ["Which dataset would you like to perform the prediction on?",
                            f"{MEDIADIR}/ques_pred_data.mp3"],
              "model_not_found": ["Sorry, but I wasn't able to find the model you requested",
                                  f"{MEDIADIR}/model_not_found.mp3"]
              }


def generate_all_files():
    for utterance in utterances.values():
        tts = gTTS(utterance[0], lang='en', tld='us')
        tts.save(utterance[1])

# Derived from source: https: // gtts.readthedocs.io / en / latest / module.html
# Last accessed: Dec 25, 2022


def generate_file(utterance):
    sound = utterances[utterance][0]
    path = utterances[utterance][1]
    tts = gTTS(sound, lang='en', tld='us')
    tts.save(path)
# Derived from source: https: // gtts.readthedocs.io / en / latest / module.html
# Last accessed: Dec 25, 2022


def say(utterance):
    path = utterances[utterance][1]
    print(path)
    os.system(f"afplay {path}")
# Derived from source: https://github.com/TaylorSMarks/playsound
# Last accessed: Dec 25, 2022



if __name__ == "__main__":
    generate_file("model_not_found")
    say("model_not_found")
