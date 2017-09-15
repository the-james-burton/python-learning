import sys
from urllib.request import urlopen


def fetch_words(url):
    # reStructuredText, sphinx
    # google python style guide
    """Fetch a list of words from a URL
    Args:
        url: URL with words
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_items(items):
    for item in items:
        print(item)


def main(url):
    # 'http://sixty-north.com/c/t.txt'
    words = fetch_words(url)
    print_items(words)

# argvparse, docopt
if __name__ == '__main__':
    main(sys.argv[1])
