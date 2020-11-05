from text_processor import TextProcessor


class TextProcessorInterface:
    def __init__(self, text):
        self.text = text
        self.processor = TextProcessor(text)

    def tokenize(self):
        return self.processor.tokenize()

    def lemmatize(self):
        return self.processor.lemmatize()

    def stem(self):
        return self.processor.stem()

    def filter_stop_words(self):
        return self.processor.filter_stop_words()

    def words_distribution(self):
        return self.processor.words_distribution()

    def most_common(self, count):
        return self.processor.most_common(count)

    def word_freq(self, word):
        return self.processor.word_freq(word)
