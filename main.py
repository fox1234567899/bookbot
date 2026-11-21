import sys
from stats import get_words_count,count_character,chars_dict_to_sorted_list

if len(sys.argv) <2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    
    print_report(get_words_count,get_book_text,chars_dict_to_sorted_list)



def get_book_text(file_path):
    with open(file_path,encoding="utf-8") as f:
        file_contents=f.read()
        return file_contents



def print_report(get_words_count,get_book_text,chars_dict_to_sorted_list):
    the_count=count_character(get_book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    get_words_count(get_book_text)
    print("--------- Character Count -------")
    the_sorted=chars_dict_to_sorted_list(the_count)
    for m in the_sorted:
        if m[0].isalpha():
            print(f"{m[0]}: {m[1]}")

    print("============= END ===============")









main()