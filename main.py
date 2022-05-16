import pandas as pd

df = pd.read_csv('nato_phonetic_alphabet.csv')

nato_dict = {row.letter:row.code for (index, row) in df.iterrows()}

input_str = list(input('Enter your name:').strip().upper())

print(input_str)

output_str = [nato_dict[letter] for letter in input_str if n in nato_dict.keys() ]

print(output_str)
