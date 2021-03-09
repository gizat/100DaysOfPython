import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet = {row.letter:row.code for (index, row) in df.iterrows()}

word = input("Enter a word: ").upper()
word_in_nato = [nato_alphabet[letter] for letter in word]
print(word_in_nato)

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

