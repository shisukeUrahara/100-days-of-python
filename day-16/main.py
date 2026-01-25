# from turtle import Turtle,Screen
from prettytable import PrettyTable
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
#
# # instantiating a turtle
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color('green')
# timmy.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# printing pokemons

table = PrettyTable()
table.add_column("Pokemon Name",["pikachu","squirtle","charmander"])
table.add_column("Pokemon Type",["electric","water","fire"])
table.align="l"

print(table)

# OOPS COFFEE MACHINE


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if drink:
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
