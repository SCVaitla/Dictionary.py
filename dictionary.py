
from PyDictionary import PyDictionary

#create an instance of PyDictionary class
dictionary=PyDictionary()

while True:
    #get the word from the user
    word = input("Enter a word (or 'q' to quit): ")
    if word == 'q':
        break
    #get the definition of the word
    definition = dictionary.meaning(word)
    if definition:
        for key in definition:
            print(f'{key}:')
            for mean in definition[key]:
                print(f'    {mean}')
    else:
        print(f"{word} not found.")
