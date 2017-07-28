import string
import re

def word_count(sentence):
    lowercased_sentence = sentence.lower()
    nopunctuation_lowercased_sentence = re.sub('[^0-9a-zA-Z]+', ' ', lowercased_sentence)
    hash_map = {}
    words = nopunctuation_lowercased_sentence.split()
    for word in words:
        if word == '':
            continue
        if hash_map.get(word) == None:
            hash_map[word] = 1
        else:
            hash_map[word] += 1
    return hash_map
