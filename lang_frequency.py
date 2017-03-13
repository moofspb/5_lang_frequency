import os
import re
import argparse
import collections


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as handler:
        return handler.read()


def get_most_frequent_words(text, number_of_common_words):
    words = re.findall(r'[\w]+', text)
    counts = collections.Counter(words)
    return counts.most_common(number_of_common_words)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Counts more common / '
                                                 'words in the text file')
    parser.add_argument('filepath', help='A path to a text file')
    parser.add_argument('number_of_common_words', help='Number of common words')
    args = parser.parse_args()
    parsed_text = load_data(args.filepath)
    most_frequent_words = get_most_frequent_words(parsed_text,
                                                  int(args.number_of_common_words))
    print('There are {} most frequent words in the text:'
          .format(args.number_of_common_words))
    for word, count in most_frequent_words:
        print("'{}': {} times".format(word, count))
