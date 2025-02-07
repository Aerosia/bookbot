

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    print(f"{num_words} words found in the document")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(s):
    words = s.split()
    return len(words)

def count_characters():
    char_dict = {}
    lowered_string = get_book_text("books/frankenstein.txt").lower()
    for char in lowered_string:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    
    return char_dict

def report():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(f"--- Begin report of {book_path} ---")
    words = count_words(text)
    print(f"{words} words found in the document")
    character_dictionary = count_characters()
    char_list = list(character_dictionary.items())
    char_list.sort(reverse=True, key=lambda x: x[1])
    for char in char_list:
        if char[0].isalpha():
            print(f"The '{char[0]}' was found {char[1]} times")
    print("--- End of report ---")
def sort_on(dict):
    return dict["char"]

report()
