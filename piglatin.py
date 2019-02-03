from nltk.corpus import words
import re

whitespace = re.compile(r'\s+')

def to_english(text):
    word_list = []
    for word in whitespace.split(text):
        word_list.append(_word_to_english(word))
    return ' '.join(word_list)

def _word_to_english(word):
    word = word[:-2]
    if word.endswith('w') and word[:-1].lower() in words.words():
        return word[:-1]
    if (word[-1]+word[:-1]) in words.words():
        return word[-1]+word[:-1]
    if (word[-2:]+word[:-2]) in words.words():
        return word[-2:]+word[:-2]
