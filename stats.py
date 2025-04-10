
def count_book_words(book_text):
    words_list = book_text.split()

    return len(words_list)

def count_each_character(book_text):
    char_count_dict = {}

    for char in book_text:
        char = char.lower()

        if char in char_count_dict:
            char_count_dict[char] += 1
        
        else:
            char_count_dict[char] = 1
    
    return char_count_dict

def sort_dict(dicty):
    chars_list = []
    for key, value in dicty.items():
        if key.isalpha():
            chars_list.append({"char": key, "count": value})
    
    def sort_on(dict):
        return dict["count"]

    chars_list.sort(reverse=True, key=sort_on)

    return chars_list

    
