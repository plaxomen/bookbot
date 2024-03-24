def main():
    book_path = "books/frankenstein.txt"
    create_report(book_path)


def create_report(path):
    text = read_file_contents(path)
    word_count = get_word_count(text)
    char_counts = get_char_frequency(text)
    sorted_char_counts = sorted(
        char_counts.items(), key=lambda tup: tup[1], reverse=True
    )

    print(f"--- Begin report of {path} ---\n")
    print(f"\t{word_count} words found in the document.\n")
    for ch, count in sorted_char_counts:
        print(f"\tThe '{ch}' character was found {count} times.")
    print("--- END REPORT ---")


def read_file_contents(file_path):
    with open(file_path) as f:
        return f.read()


def get_word_count(text):
    return len(text.split())


def get_char_frequency(text):
    char_counts = {}
    for ch in text:
        if ch.isalpha():
            lower_ch = ch.lower()
            if lower_ch in char_counts:
                char_counts[lower_ch] += 1
            else:
                char_counts[lower_ch] = 1
    return char_counts


main()
