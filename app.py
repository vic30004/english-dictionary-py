import json 
from difflib import get_close_matches

data = json.load(open("data.json"))




def get_word(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])

    else:
        return "Ooops something went wrong. Make sure your text is corrext"

word = input("Enter word: ")

print(get_word(word))