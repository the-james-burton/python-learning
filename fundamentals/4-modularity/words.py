#!/usr/bin/env python3
"""Fetch and print all words in a given URL
Usage:
    python3 words.py <URL>
"""

import sys
from urllib.request import urlopen


def fetch_words(url):
    # reStructuredText, sphinx
    # google python style guide
    """Fetch a list of words from a URL
    Args:
        url: URL with words
    Return
        A list of words
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_list(list):
    """Print the given list, one per line
    Args:
        The list to print
    """
    for item in list:
        print(item)


def main(url):
    """Print each word from the given URL
    Args:
        The URL to fetch the words from
    """
    # 'http://sixty-north.com/c/t.txt'
    words = fetch_words(url)
    print_list(words)

# argvparse, docopt
if __name__ == '__main__':
    # The 0th arg is the module filename,
    # hence we use 1 here to get the first program arg...
    main(sys.argv[1])
