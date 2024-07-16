def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print_report(book_path)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    character_dict = {}
    for char in text:
        to_lower = char.lower()
        if to_lower in character_dict:
            character_dict[to_lower] += 1
        else:
            character_dict[to_lower] = 1
    return character_dict

def sort_on(dict):
    return dict["num"]

def print_report(path):
    text = get_book_text(path)
    char_dict = count_characters(text)
    words = count_words(text)
    char_list = []

    print(f"--- Begin report of {path} ---")
    print(f"{words} words found in the document")

    for char in char_dict:
        char_list.append({"char" : char, "num" : char_dict[char]})

    char_list.sort(reverse=True, key=sort_on)

    for char in char_list:
        if char["char"].isalpha():
            print(f"The '{char['char']}' character was found {char['num']} times")
    print("--- End report ---")



main()