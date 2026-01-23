from game_data import data
import random

logo = r"""
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = r"""
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""


is_game_over=False
score=0
element_1 = data.pop(random.randint(0, len(data) - 1))
current_winner= element_1
# print(f"compare {element_1.name} , a {element_1.description} from {element_1.country}")
# print(vs)
# print(f"compare {element_2.name} , a {element_2.description} from {element_2.country}")

while not is_game_over:
    print(logo)

    if(not len(data)):
        print(f"You won , your score is {score}")
        break

    element_2 = data.pop(random.randint(0, len(data) - 1))
    print(f"compare {current_winner['name']} , a {current_winner['description']} from {current_winner['country']}")
    print(vs)
    print(f"compare {element_2['name']} , a {element_2['description']} from {element_2['country']}")
    user_input=input("Who has more followers? Type 'A' or 'B' ")
    if user_input=='A':
        if(current_winner['follower_count'] > element_2['follower_count']):
            score+=1
        else:
            is_game_over=True
            print(f" You lost , your score is {score}")
    elif user_input=='B':
        if(element_2['follower_count'] > current_winner['follower_count']):
            current_winner=element_2
            score+=1
        else:
            is_game_over=True
            print(f" You lost , your score is {score}")
    else:
        print("invalid input")

