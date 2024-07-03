"""
Allows you to replace words in a sentence
"""

def replace_word():
    """
    Takes a sentence and returns a new sentence that replaces one word
    """
    og_sentence = input("Type out a sentence: ")
    replaced_word = input("Which word would you like to replace? ")
    new_word = input("Which word would you like to replace that word with? ")
    return og_sentence.replace(replaced_word, new_word)

print(replace_word())
