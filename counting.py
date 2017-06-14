def words(string):
    the_words = string.split()
    the_words = [int(word) if word.isdecimal() else word for word in the_words]

    return {word: the_words.count(word) for word in the_words}

