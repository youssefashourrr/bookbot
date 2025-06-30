from stats import get_word_count, get_char_counts, get_report
import sys


def get_book_text(book):
    with open(book) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    char_counts = get_char_counts(text)
    report = get_report(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for char_info in report:
        print(f"{char_info['char']}: {char_info['num']}")
    
    print("============= END ===============")


if __name__ == "__main__":
    main()