import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def dict(word):
    word = word.lower() # converting the entered words in a lowecase
    if word in data:
        return data[word]
    elif word.title() in data:      #if user entered "texas" this will check for "Texas" as well. For nouns(Delhi, Paris etc.)
        return  data[word.title()]
    elif word.upper() in data:      #in case user enters words like USA or NATO
        return data[word.upper()]   
    elif len(get_close_matches(word, data.keys(), cutoff=0.8)) > 0:
        # suggesting words to user, if they make a spelling mistake
        yn = input("Did you mean %s instead? Enter Y for yes, N for no: " % get_close_matches(word, data.keys(), cutoff=0.8)[0])
        if yn == "Y":
            # returning close matches from the databse with an accuracy of 0.8
            return data[get_close_matches(word, data.keys(), cutoff=0.8)[0]]
        elif yn == "N":
            return "The word doesn't exits. Please double check the word."
        else:
            return "We didn't understand your response."
    else:
        return "The word doesn't exist. Please double check the word."

user_input = input("Enter the word: ")
output = dict(user_input)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)



