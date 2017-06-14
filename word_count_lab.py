#word count

def words(word_list):
    word_dict = {}
    word_list=word_list.split()
    for word in word_list:
        try: #if the word is convertable to an int run the word count and keep it as int in dictionary
            if word in word_dict:
                word_dict[int(word)] = word_dict[int(word)] + 1
            else:
                word_dict[int(word)] = 1
        except ValueError: #string types cause value errors so will be kept as str type in dictionary
            if word in word_dict:
                word_dict[str(word)] = word_dict[str(word)] + 1
            else:
                word_dict[str(word)] = 1
    return word_dict