import pandas as pd

df = pd.read_csv('nato_phonetic_alphabet.csv')

nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}


# ### MY VERSION:
# isAString = False
# input_str =''
#
# while not isAString:
#     try:
#         input_str = list(input('Enter your name:').strip().upper())
#         output_str = [nato_dict[letter] for letter in input_str]
#         isAString = True
#     except KeyError:
#         print('Sorry, only letters from the alphabet please!\n')
#     else:
#         print(output_str)

# ### PROPOSED VERSION:

def generate_nato():
    input_str = list(input('Enter your name:').strip().upper())
    try:
        output_str = [nato_dict[letter] for letter in input_str]
    except KeyError:
        print('Sorry, only letters from the alphabet please!\n')
        generate_nato()
    else:
        print(output_str)


generate_nato()
