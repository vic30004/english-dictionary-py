import json 
from difflib import get_close_matches

data = json.load(open("data.json"))




def get_word(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])

        if yn.lower()=="y":
              return data[get_close_matches(w, data.keys())[0]]
        elif yn.lower()=='n':
              return "Ooops something went wrong. Make sure your text is correct"
        else: 
              return "I didn't get that, please try again"
    else:
        return "Ooops something went wrong. Make sure your text is correct"

word = input("Enter word: ")

print(get_word(word))