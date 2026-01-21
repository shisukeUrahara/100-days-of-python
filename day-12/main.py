enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

# block and local scopes

if(True):
    name='shisuke'

print(name) # this is ok since name is in block scope so available here

def print_name():
    if(True):
        name2='shisuke'

# print(name2) #this gives error now since name2 is in local scope of print_name function


# is_prime
def is_prime(num):
    for number in range(2, num - 1):
        if (num % number == 0):
            return False

    return True


variable = 75
print(f"is_prime {is_prime(variable)}")

# number guessing game
import random

def play_num_guessing_game():
    chosen_number = random.randint(1, 100)
    game_difficulty = input('Choose a difficulty level (easy or  hard): ')
    num_attempts = 10

    if(game_difficulty != "easy" and game_difficulty != "hard"):
        print("Invalid choice")
        play_num_guessing_game()


    if (game_difficulty == 'hard'):
        num_attempts = 5

    while (num_attempts>0):
        choice = int(input(f"Please choose a number between 1 and 100: "))
        if (choice == chosen_number):
            print('You got it!')
        else:
            if (choice > chosen_number):
                print("Too High!")
            else:
                print("Too Low!")
            num_attempts = num_attempts - 1
            if(not num_attempts):
                print(f'Attempts over , You lost! the correct answer was {chosen_number}')

play_num_guessing_game()

