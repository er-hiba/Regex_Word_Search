import re

def search_word(string, word):
    if re.search(r'\b' + re.escape(word) + r'\b', string):
        return True
    else:
        return False

# Taking input from the user
text = input("Enter a text: ")
word = input("Enter a word to search: ")

result = search_word(text, word)
if result:
    print(f"The word '{word}' was found in the text.")
else:
    print(f"The word '{word}' was not found in the text.")

