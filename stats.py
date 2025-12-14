def get_num_words(text):
    lower_text = text.lower()
    word_list = lower_text.split()
    number_of_words = len(word_list)


    result = {}
    for word in word_list:
        for letter in word:
            if letter.isalpha():
                if letter not in result:
                    result[letter] = 1
                else:
                    result[letter] +=1
            else:
                continue
    return result,number_of_words

def title(path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")



def report (path,letters):
    title(path)
    print("----------- Word Count ----------")
    print(f"Found {letters[1]} total words")
    print("--------- Character Count -------")
    dict_letters = letters[0]
    sorted_letters = dict(sorted(dict_letters.items(), key = lambda item: item[1], reverse=True ))
    for k,v in sorted_letters.items():
        print(f"{k}: {v}")
