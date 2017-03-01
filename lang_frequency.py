import os
import re
import argparse
import collections


NUMBER_OF_WORDS = 10


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as handler:
        return handler.read()


def get_most_frequent_words(text):
    words = re.findall(r'[\w]+', text)
    counts = collections.Counter(words)
    return counts.most_common(NUMBER_OF_WORDS)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Counts 10 more common / '
                                                 'words in the text file')
    parser.add_argument('filepath', help='A path to a text file')
    args = parser.parse_args()
    parsed_text = load_data(args.filepath)
    most_frequent_words = get_most_frequent_words(parsed_text)
    print('There are 10 most frequent words in the text:')
    for word, count in most_frequent_words:
        print("'{}': {} times".format(word, count))
