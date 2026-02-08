import pandas

content = pandas.read_csv("nato_phonetic_alphabet.csv")

# convert it to dictionary
phonetics_dict={row.letter:row.code for (index,row) in content.iterrows() }
print(phonetics_dict)

name = input("Please enter your name: ")
name_list= [phonetics_dict[letter.upper()] for letter in name]
print(name_list)