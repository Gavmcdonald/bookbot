def get_word_count(book_content):
    return len(book_content.split())

def get_num_characters(book_content):
    book_content = book_content.lower()
    characters = {}
    for word in book_content:
        
        for letter in word:
            if letter not in characters:
                characters[letter] = 1
            else:
                characters[letter] = characters[letter] +1
    return characters

def sort_on(item):
    return(item["num"])

def sort_list(character_list):
    sorted_list = []
    for character,num in character_list.items():
        sorted_list.append({"char":character,"num":num})
    sorted_list.sort(key=sort_on,reverse=True)
    return sorted_list

    # print(book_content)