#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
names=[]

with open("./Input/Names/invited_names.txt", "r") as f:
    names = f.read().splitlines()
    # print(names)

# reading starter template
with open("./Input/Letters/starting_letter.txt", "r") as f:
    template=f.read()


for name in names:
    with open(f"./Output/ReadyToSend/invited_{name}", "w") as f:
        letter = template.replace("[name]", name)
        print(letter)
        f.write(letter)



#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp