import re

VOWELS = "aeiou"

def to_piglatin(text):
    word_list = []
    for word in text.split():
        word_list.append(_word_to_piglatin(word))
    return ' '.join(word_list)

def _word_to_piglatin(word):
    if word[0] in VOWELS:
        return word+'way'
    for i in range(len(word)):
        if word[i] in VOWELS:
            return word[i:]+word[:i]+'ay'
