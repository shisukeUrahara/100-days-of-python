import random

# print(random.randint(1,10))
# print(random.random())
# print(random.uniform(1,21))
# print(random.randrange(1,100))


# heads or tails
random_seed= random.random()
if(random_seed < 0.5):
    print('HEADS')
else:
    print('TAILS')

# lists
fruits=['apple','orange','grape']
print(fruits[0])
print(fruits[1])
print(fruits[-1]) # last item in list
print(fruits[-2]) # second last item in list
fruits.extend(['Mango','Chiku'])
print(fruits)

# billing roulette
friends=['alice','bob','charlie','david','emanuelle']
randomIndex=random.randint(0,len(friends)-1)
print(f"the bill will be paid by {friends[randomIndex]}")
# alt method
print(f"the bill will be paid by {random.choice(friends)}")

# rock paper scissors game
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

print('Welcome to the Rock Paper Scissors game!')
choices=[rock,paper,scissors]
user_choice= int(input('Enter the game and choose. 0 for rock , 1 for paper and 2 for scissors.\n'))
print('You chose',choices[user_choice]+'\n')
computer_choice = random.randint(0,2)
print('Computer chose '+choices[computer_choice]+'\n')
winning_choices=[['DRAW','LOSE','WIN'],
                 ['WIN','DRAW','LOSE'],
                 ['LOSE','WIN','DRAW']
                 ]
result=winning_choices[user_choice][computer_choice]
if(result=='DRAW'):
    print('Its a draw')
else:
    print('You '+result)


