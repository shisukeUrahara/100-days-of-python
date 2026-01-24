from operator import truediv

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


is_machine_on= True
money=0

def print_resources_and_money():
    for key, value in resources.items():
        print(f"{key}: {value}ml")

    if(money>0):
        print(f"You earned ${money}")

def check_if_enough_assets(option):
    ingredients_needed = MENU[option]["ingredients"]
    for ingredient, amount_needed in ingredients_needed.items():
        if resources.get(ingredient, 0) < amount_needed:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


def processed_money_correctly(choice):
    money_needed= MENU[choice]['cost']
    current_money=0
    print(f"you need ${money_needed}")
    quarter_count=int(input('Enter number of quarters'))
    dime_count=int(input('Enter number of dimes'))
    nickel_count=int(input('Enter number of nickel'))
    penny_count=int(input('Enter number of pennies'))

    current_money= current_money + quarter_count*0.25+dime_count*0.10+nickel_count*0.05+penny_count*0.01
    if(money_needed>current_money):
        print(f"Sorry that's not enough money. Money refunded.")
        return False
    elif(money_needed<current_money):
        print(f"Payment processed , returned change ${(current_money-money_needed)}")
        return True
    else:
        print('payment processed')
        return True

def make_dish(option):
    for ingredient, amount in MENU[option]["ingredients"].items():
        resources[ingredient] -= amount
    print(f"Here is your {option}. Enjoy!")


def take_money_and_make_option(input):
    if(processed_money_correctly(input)):
        make_dish(input)


while(is_machine_on):
    user_input= input('What would you like? (espresso/latte/cappuccino):')
    if(user_input=='report'):
        print_resources_and_money()
    elif(user_input=='off'):
        is_machine_on = False
        break
    elif(user_input !='espresso' and user_input!='latte' and user_input!='cappuccino'):
        print('Invalid input ')
        continue
    else:
        if(check_if_enough_assets(user_input)):
            take_money_and_make_option(user_input)



