from gtts import gTTS
from playsound import playsound

def generate_files():
    greeting = "Hello! Jarvis at your service"
    tts1 = gTTS(greeting)
    tts1.save("greeting.mp3")

    ques_func_type = \
        "What would you like to do? Calculate statistical key figures, generate a visualization or predict?"
    tts2 = gTTS(ques_func_type)
    tts2.save("ques_func_type.mp3")

    ques_func = "What exactly would you like me to calculate?"
    tts3 = gTTS(ques_func)
    tts3.save("ques_func.mp3")

    ques_ds = "Which data set should I use?"
    tts4 = gTTS(ques_ds)
    tts4.save("ques_ds.mp3")

    request_repetition = "I'm not sure I understand. Could you repeat please?"
    tts5 = gTTS(request_repetition)
    tts5.save("request_repetition.mp3")


def greet():
    playsound("/Users/joshua/ws/jarvis/src/jarvis/greeting.mp3")
    return False


def ask_func_type():
    playsound("ques_func_type.mp3")


def ask_func():
    playsound("ques_func.mp3")


def ask_ds():
    playsound("ques_ds.mp3")


def ask_repeat():
    playsound("request_repetition.mp3")


if __name__ == "__main__":
    greet()
    ask_func_type()
    ask_func()
    ask_ds()
    ask_repeat()
