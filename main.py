from stats import count_book_words, count_each_character, sort_dict
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_contents = get_book_text(sys.argv[1])
        word_count = count_book_words(file_contents)

        print(f"Found {word_count} total words")

        count_chars = count_each_character(file_contents)
        sorted_dict = sort_dict(count_chars)

        for item in sorted_dict:
            print(f"{item["char"]}: {item["count"]}")


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    
    return file_contents



main()

