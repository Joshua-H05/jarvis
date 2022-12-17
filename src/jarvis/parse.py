from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import re

from jarvis import compute as c


class Utterance:
    def __init__(self, utterance):
        self.reformatted = None
        self.utterance = utterance
        self.intents = ("calculate meanz",
                        "calculate median",
                        "calculate mode",
                        "calculate range",
                        "calculate standard deviation",
                        "plot histogram",
                        "plot scatter plot",
                        "plot pie chart")

        self.stopwords = set(stopwords.words("english"))
        self.filtered = []

    def reformat(self):
        self.utterance = re.sub(r'[^\w\s]', " ", self.utterance.lower())
        words = word_tokenize(self.utterance)
        for word in words:
            if word not in self.stopwords:
                self.filtered.append(word)

    def run(self):
        pass

    def parse_intent(self):
        if self.reformatted in self.intents:
            self.run()


mean_command = Utterance(utterance="Could, you please compute the mean of the dataset X?")
mean_command.reformat()
reformatted = mean_command.filtered
print(reformatted)
