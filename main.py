import sys
from stats import num_of_words,count_characters,sort_on

def main():
    num_of_arguments = len(sys.argv)
    if num_of_arguments != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path_book = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path_book}...")
    print("----------- Word Count ----------")
    words = num_of_words(file_path_book)
    var = count_characters(words)
    print("--------- Character Count -------")
    list_of_dict = []
    for char,count in var.items():
        dictionary = {"char": char, "num": count}
        list_of_dict.append(dictionary)
    list_of_dict.sort(reverse=True,key=sort_on)
    for entry in list_of_dict:
        char = entry["char"]
        num = entry["num"]
        if char.isalpha():
            print(f"{char}: {num}")
    print("============= END ===============")

main()