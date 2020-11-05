from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk import FreqDist


class TextProcessor:
    def __init__(self, text):
        self.text = text
        self.lemmatizer = WordNetLemmatizer()
        self.stemmer = PorterStemmer()
        self.stop_words = set(stopwords.words('english'))

    def tokenize(self):
        return word_tokenize(self.text)

    def lemmatize(self):
        return list(map(lambda w: self.lemmatizer.lemmatize(w), self.tokenize()))

    def stem(self):
        return list(map(lambda w: self.stemmer.stem(w), self.tokenize()))

    def filter_stop_words(self):
        return [w for w in self.tokenize() if not w in self.stop_words]

    def words_distribution(self):
        return FreqDist(self.tokenize()).items()

    def most_common(self, count):
        return FreqDist(self.tokenize()).most_common(count)

    def word_freq(self, word):
        return FreqDist(self.tokenize())[word]