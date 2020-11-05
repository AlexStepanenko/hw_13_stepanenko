import argparse
from text_processor_interface import TextProcessorInterface


def run():
    parser = argparse.ArgumentParser(description='Parse args from json file.')
    parser.add_argument('--path', type=str, required=True, help='Path to file')
    args = parser.parse_args()

    # https: // www.gutenberg.org / files / 46 / 46 - 0.
    # txt
    text = open(args.path).read()

    processor = TextProcessorInterface(text)

    print(processor.tokenize())
    print(processor.lemmatize())
    print(processor.stem())
    print(processor.filter_stop_words())
    print(processor.words_distribution())
    print(processor.most_common(10))
    print(processor.word_freq('being'))


if __name__ == '__main__':
    run()
