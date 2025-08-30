import sys
from stats import count_words, count_chars, sort_chars


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_book = sys.argv[1] 
    text = get_book_text(path_to_book)
    num_words = count_words(text)
    chars_dict = count_chars(text)
    result = sort_chars(chars_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for blob in result:
        char = blob["char"]
        if char.isalpha():
            num = blob["num"]
            print(f"{char}: {num}")

    print("============= END ===============")


main()
