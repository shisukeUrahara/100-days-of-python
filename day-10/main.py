def format_name_to_upper_case(first_name,last_name):
    """This is the docstring , now it shows up when you ctrl + hover over this function"""
    return (first_name + " " + last_name).upper()

def format_name_to_title_case(first_name,last_name):
    return (first_name + " " + last_name).title()

formatted_name = format_name_to_upper_case("shisuke","urahara")
title_case_name= format_name_to_title_case("shisuke","urahara")
print(formatted_name)
print(title_case_name)

#  checking leap year
def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0


year = 2000

is_leap = is_leap_year(year)
print(f"year {year} , is it leap year ? {is_leap} ")

# calculator

logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

print(logo)

calculator_on=True
current_result=0
continue_option=False

while(calculator_on):
    if(not continue_option):
        number_1 = int(input("Enter a number: "))
    operation= input(""" Pick an operation
    +
    -
    /
    *
    """)
    number_2=int(input("Enter another number: "))
    if(not continue_option):
        if (operation == "+"):
            current_result = number_1 + number_2
        elif (operation == "-"):
            current_result = number_1 - number_2
        elif (operation == "/"):
            current_result = number_1 / number_2
        elif (operation == "*"):
            current_result = number_1 * number_2
        else:
            print("you chose an invalid operation")
    else:
        if (operation == "+"):
            current_result = current_result + number_2
        elif (operation == "-"):
            current_result = current_result - number_2
        elif (operation == "/"):
            current_result = current_result / number_2
        elif (operation == "*"):
            current_result = current_result * number_2
        else:
            print("you chose an invalid operation")


    print("The result is ",current_result)

    continue_session= input("do you want to continue calculating or start again? answer y for continuing and n for starting again")
    if(continue_session.lower()=="n"):
        continue_option=False
    elif(continue_session.lower()=="y"):
        continue_option=True
    else:
        print('You chose an invalid option')

