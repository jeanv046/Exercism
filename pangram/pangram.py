import string
def is_pangram(sentence):
    return all(char in sentence.lower() for char in string.ascii_lowercase)