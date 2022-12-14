import pyttsx3

def greeting():
    engine = pyttsx3.init()
    engine.say("Hello")
    engine.runAndWait()

greeting()
