import os
import re
import sys
import collections


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as handler:
        return handler.read()


def get_most_frequent_words(text):
    words = re.findall(r'[a-zA-Zа-яА-Я]+', text)
    counts = collections.Counter(words)
    most_common_words = counts.most_common(10)
    return most_common_words


if __name__ == '__main__':
    most_frequent_words = get_most_frequent_words(load_data(sys.argv[1]))
    print('There are 10 most frequent words in the text:')
    for word, count in most_frequent_words:
        print("'{}': {} times".format(word, count))
