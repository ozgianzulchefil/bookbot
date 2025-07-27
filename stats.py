def get_book_contents(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def num_of_words(file_path_book):
    words = (get_book_contents(file_path_book)).split()
    num_of_words = len(words)
    print(f"Found {num_of_words} total words")
    return words

def count_characters(words):
    count_characters = {}
    for word in words:
        for character in word:
            character = character.lower()
            if character in count_characters:
                count_characters[character] = count_characters[character] + 1
            else:
                count_characters[character] = 1
    return count_characters

def sort_on(items):
        return items["num"]