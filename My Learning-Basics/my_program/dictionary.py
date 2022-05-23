import requests

word = input("PLease input the word that you want search for in a Dictionary: ")
url = "https://api.dictionaryapi.dev/api/v2/entries/en/{0}".format(word)

api_response = requests.get(url)
my_dictionary = api_response.json()

for dictionary in my_dictionary:
    print(dictionary)
    print(f"Word: {dictionary['word']} Definition: {dictionary['meanings[0].definitions[0].definition']}")
