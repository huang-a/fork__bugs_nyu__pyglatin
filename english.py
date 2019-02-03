import re

vowels = 'aeiou'

def to_piglatin(text):
    word_list = []
    for word in whitespace.split(text):
        word_list.append(_word_to_english(word))
    return ' '.join(word_list)

def _word_to_piglatin(word):
    if word[0] in vowels:
        return word+'way'
    for i in range(len(word)):
        if word[i] in vowels:
            return word[i:]+word[:i]+'ay'
