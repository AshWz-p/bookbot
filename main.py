import sys
from stats import get_num_words
from stats import get_count_characters
from stats import create_report

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    create_report()
main()
