# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

num=int(input("enter a number\n"))
isEven=num%2==0
if(isEven):
    print("The number is even")
else:
    print("The number is odd")


# # bmi test
weight = 85
height = 1.85

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇
if(bmi<18.5):
    print("underweight")
elif(bmi<24.9):
    print("normal weight")
else:
    print("overweight")

# # nested and multiple if else
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill=0

if(size=="S"):
    bill+=15
elif(size=="M"):
    bill+=20
elif(size=="L"):
    bill+=25

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")


#  Treasure hunt
print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice_1= input("Do you want to go left or right\n")
if(choice_1 == "left"):
    print("You fell into a hall and died. GAME OVER")
elif(choice_1 == "right"):
    choice_2=input("Do you want to swim or wait for a boat? \n")
    if(choice_2 == "swim"):
        print("You drowned. GAME OVER")
    elif(choice_2 == "wait"):
        choice_3=input("You see 3 doors , red , blue or green . which one do you choose? \n")
        if(choice_3 == "red" or choice_3 == "blue"):
            print("You fell into a trap . GAME OVER")
        else:
            print("You found the treasure. HORRAY! YOU WON!")
