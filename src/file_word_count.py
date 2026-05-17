import sys


def parse_args() -> list[str]:
    return sys.argv[1]


def read_file(filename: str) -> list[str]:
    try:
        with open(filename, "r") as fobj:
            words = []
            for line in fobj:
                target = line.split()
                for word in target:
                    words.append(word)
            return words

    except FileNotFoundError as e:
        print(e)


def normalize_words(words):
    pass


def word_frequencies(words):
    pass


def print_top_words(freqs, limit=10):
    pass


def main():
    # Parse command-line arguments
    filename = parse_args()

    # Read file contents
    word_list = read_file(filename)
    print(len(word_list))

    # Normalize words

    # Compute frequencies

    # Print results


if __name__ == "__main__":
    main()
