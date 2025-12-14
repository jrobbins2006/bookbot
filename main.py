import sys
from stats import get_num_words
from stats import report


def get_book_text(path_to_file):
    with open (path_to_file) as f:
        file_contest = f.read()
    return file_contest



def main():
    if len(sys.argv) > 1:
        book_path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(book_path)
    raw_letters = get_num_words(book_text)
    # print(raw_letters[1])
    report(book_path, raw_letters)

    


main()