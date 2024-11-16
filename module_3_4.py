def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        if root_word.upper() in i.upper():
            same_words.append(i)
    return same_words

print(single_root_words('Rich', 'richer', 'iching', 'riched', 'ching'))