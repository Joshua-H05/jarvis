import pyttsx3 as v2s
import speech_recognition as sr


def recognise():
    r = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        utterance = r.listen(source)
        return Speech(utterance)


class Speech:
    def __init__(self, utterance):
        self.utterance = utterance
        self.greetings = ("Hello", "Hellow Jarvis", "Hey Jarvis", "Jarvis")
        self.requests = {}  # Dict with requests from the user and the corresponding commands (commands stored in
        # separate pyfile

    def log_speech(self):  # write user input into Json file
        pass

    def simplify(self):
        # Use libraries like NLTK to parse the request, and discard all irrelevant words
        pass

    def respond(self):
        engine = v2s.init()
        if self.utterance in self.greetings:
            engine.say("Hello, how may I help you?")
        elif self.utterance in self.requests:
            # if self.utterance in self.requests:
            pass
        else:
            # if self.utterance not in self.greetings and self.utterance not in self.requests:
            engine.say("Sorry, I'm not able to do that yet.")


if __name__ == "__main__":
    pass
