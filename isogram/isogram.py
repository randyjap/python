def is_isogram(word):
    hashmap = {}
    for letter in word:
        if hashmap.get(letter.lower()) != None:
            return False
        if letter.isalpha():
            hashmap[letter.lower()] = True
    return True
