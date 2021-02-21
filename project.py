import json
from difflib import get_close_matches
data=json.load(open("data.json"))
def translate(word):
    word=word.lower()
    if word in data:
       return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys()))>0:

        choice=input("Did you mean %s instead ? Enter Y for yes and N for no." %get_close_matches(word,data.keys())[0])
        choice=choice.upper()
        if choice == "Y":
            return data[get_close_matches(word,data.keys())[0]]
        elif choice == "N":
            return "Word not found!,please double check it"
        else:
            return "We didn't get that!"

    else:
        return "Word not found!,please double check it"

ch = input("Do you want to run the program,Y for yes and N for no: ")
ch = ch.upper()
while ch == "Y":
    word = input("Enter any word: ")
    output = (translate(word))
    if type(output) == list:
        for item in output:
            print(item)
        ch = input("Do you want to run the program again,Y for yes and N for no: ")
        ch = ch.upper()
        while ch =="N":
            print("Thank you for using our program!")
            break

    else:
        print(output)
