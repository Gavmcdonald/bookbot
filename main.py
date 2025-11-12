from stats import get_word_count, get_num_characters, sort_list
import sys

def get_book_text(path):
    with open(path) as f:
        book_content = f.read()
    return book_content

def main():

    if len(sys.argv) !=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    content = (get_book_text(path))
    count =get_word_count(content)
    sorted_list = sort_list(get_num_characters(content))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        char = item["char"]
        num = item["num"]
        if(char.isalpha()):
            print(f"{char}: {num}")

main()