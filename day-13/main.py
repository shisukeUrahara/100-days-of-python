def my_function():
    for i in range(1, 20):
        if i == 20:
            print("You got it")


my_function()

# debugged the issue range is between 1-20 , so max i will be 19 and it will never reach 20
# solution , change range from 1-21 , so i will be 1-20
def my_function2():
    for i in range(1, 21):
        if i == 20:
            print("You got it")

my_function2()

# reproduce the bug
from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# issue above is dice_num will range from 1-6 and index of dice_images range from 0-5
# solution , use dice_num by varying it from 0-5
dice_num= randint(0,5)
print(dice_images[dice_num])


# are you genz
#
# year = int(input("What's your year of birth?"))
#
# if year > 1980 and year < 1994:
#     print("You are a millennial.")
# elif year > 1994:
#     print("You are a Gen Z.")
# the issue above is that nothing is printed when user enters1994
# solution , either make millenial <=1994 or make genz >=1994


# year = int(input("What's your year of birth?"))
#
# if year > 1980 and year < 1994:
#     print("You are a millennial.")
# elif year >= 1994:
#     print("You are a Gen Z.")
#
# # fix the errors
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# using debugger

import random

def add(a,b):
    return a+b

def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = add(new_item, item)
        b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])





