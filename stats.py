import sys
def get_book_text():
    with open(sys.argv[1]) as f:
        file_contents = f.read()
        return file_contents

def get_num_words():
    num_words = len(get_book_text().split())
    print(f"Found {num_words} total words")
    return num_words

def get_count_characters():
    all_characters = {}
    words = get_book_text().lower().split()
    # print(f"All characters:\n{words}")
    #loop for counting each character
    for word in words: 
        for character in word:
            if character in all_characters: #if the character already exists in the dict, then it increments by 1
                all_characters[character] += 1
            else: #otherwise it is initialised as 1
                all_characters[character] = 1
    # print(all_characters)
    return all_characters

def sort_chars(char_dict):
    lst = []
    for character, count in char_dict.items():
        single_characters = {character: count}
        lst.append(single_characters)
    lst.sort(key=sort_on, reverse=True)
    # print(lst)
    return lst

def sort_on(dict):
    return list(dict.values())[0]

def create_report():
    sorted_list = sort_chars(get_count_characters())
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    get_num_words()
    print("--------- Character Count -------")
    
    # Now loop through your sorted char_list
    for char_dict in sorted_list:
        for char, count in char_dict.items():
            if char.isalpha():  # Only print alphabetic characters
                print(f"{char}: {count}")
    
    print("============= END ===============")