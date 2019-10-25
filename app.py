import json
from difflib import get_close_matches

# Load in our file data
file_data = open("data.json")
data = json.load(file_data)
file_data.close()


def get_definition(word):
    """Gets a definition of the inputted word from the dictionary."""
    lowercase = word.lower()
    capitalized = word.title()  # Proper nouns like state names
    upper = word.upper()  # Acronyms like USA
    if lowercase in data:
        return data[lowercase]
    elif capitalized in data:
        return data[capitalized]
    elif upper in data:
        return data[upper]
    elif len(get_close_matches(lowercase, data.keys())) > 0:
        confirm = input("Did you mean %s instead? (Y/N): " % get_close_matches(lowercase, data.keys())[0]).lower()
        if confirm == "y":
            return data[get_close_matches(lowercase, data.keys())[0]]
        elif confirm == "n":
            return "The word was not found in the dictionary. Check if you have misspelled it."
        else:
            return "We didn't understand your input."
    else:
        return "The word was not found in the dictionary. Check if you have misspelled it."


search = input("Enter a word: ")
definition = get_definition(search)

# Output can be a list or a string, so handle both instances.
if isinstance(definition, list):
    for item in definition:
        print(item)
else:
    print(definition)
