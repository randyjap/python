def is_pangram(string):
    hashmap = {}
    lowercase_string = string.lower()
    for letter in lowercase_string:
        if letter.isalpha() == False:
            continue
        hashmap[letter] = True
    return len(hashmap) == 26
