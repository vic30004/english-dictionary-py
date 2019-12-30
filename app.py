import json 
data = json.load(open("data.json"))

print(data['rain'])


def get_word():
  userInp = str(input("What word are you looking for ?"))
  try:
    for word in data[userInp]:
            print(f"{userInp}: {word}")
  except:
      print("oops, something went wrong. Make sure your text is correct!")

get_word()