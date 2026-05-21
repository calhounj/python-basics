import sys


def parse_args() -> str:
    return sys.argv[1]


def read_file(filename: str) -> list[str] | None:
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


def normalize_words(words: list[str]) -> list[str]:
    normal_words = []
    for word in words:
        normal_words.append(word.lower())
    return normal_words


def word_frequencies(words: list[str]) -> dict[str, int]:
    freq_dict = {}
    for word in words:
        if word not in freq_dict:
            freq_dict[word] = 1
        else: freq_dict[word] += 1
    return freq_dict


def print_top_words(freqs: dict[str, int], limit=10) -> None:
    sorted_desc = sorted(freqs.items(), key=lambda item: item[1], reverse=True)
    for pair in sorted_desc[:limit]:
        print(f"{pair[0]}: {pair[1]}")


def main():
    # Parse command-line arguments
    filename = parse_args()

    # Read file contents
    word_list = read_file(filename)
    if word_list is None:
        return

    # Normalize words
    lower_words = normalize_words(word_list)

    # Compute frequencies
    frequencies = word_frequencies(lower_words)

    # Print results
    print_top_words(frequencies, 5)


if __name__ == "__main__":
    main()
