from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords


class Utterance:
    def __init__(self, utterance):
        self.utterance = utterance
        self.intents = {}
        self.stopwords = set(stopwords.words("english"))
        self.filtered = []

    def reformat(self):
        words = word_tokenize(self.utterance)
        for word in words:
            if word not in self.stopwords:
                self.filtered.append(word)

    def parse_intent(self, reformatted):
        pass
