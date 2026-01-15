import random

word_list = ["aardvark", "baboon", "camel"]
#
# # TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
random_index=random.randint(0,len(word_list)-1)
chosen_word = word_list[random_index]
print(chosen_word)
#
# # TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
game_ended=False
game_end_reason='You lost'
array_result=["_"]*len(chosen_word)
num_of_lives_remaining= len(chosen_word)
initial_lives = len(chosen_word)




def end_game(reason):
    print("************ GAME OVER ************** ")
    print(f"{reason}")


def get_matching_indices(chosen_word,guessed_word):
    # print(f"get_matching_indices called with chosen word {chosen_word}, guessed word {guessed_word}")
    result=[]
    for index,word  in enumerate(chosen_word):
        # print(f"{index} -> {word}")
        if(word == guessed_word):
            result.append(index)


    return result


def display_hangman(lives_remaining, initial_lives):
    """Display hangman ASCII art based on lives remaining"""
    # Calculate which stage of hangman to show (6 stages total)
    # Map lives to stages proportionally
    lives_lost = initial_lives - lives_remaining
    # Convert to 6 stages (0-5)
    stage = int((lives_lost / initial_lives) * 6)
    stage = min(stage, 5)  # Cap at stage 5 (fully drawn)
    
    hangman_stages = [
        # Stage 0: No body parts
        """
           +---+
           |   |
               |
               |
               |
               |
         =========
        """,
        # Stage 1: Head
        """
           +---+
           |   |
           O   |
               |
               |
               |
         =========
        """,
        # Stage 2: Head + Body
        """
           +---+
           |   |
           O   |
           |   |
               |
               |
         =========
        """,
        # Stage 3: Head + Body + Left Arm
        """
           +---+
           |   |
           O   |
          /|   |
               |
               |
         =========
        """,
        # Stage 4: Head + Body + Both Arms
        """
           +---+
           |   |
           O   |
          /|\\  |
               |
               |
         =========
        """,
        # Stage 5: Complete (Head + Body + Arms + Left Leg)
        """
           +---+
           |   |
           O   |
          /|\\  |
          /    |
               |
         =========
        """,
        # Stage 6: Fully hanged (Head + Body + Arms + Both Legs)
        """
           +---+
           |   |
           O   |
          /|\\  |
          / \\  |
               |
         =========
        """
    ]
    
    # Show stage 6 only when lives are 0
    if lives_remaining == 0:
        print(hangman_stages[6])
    else:
        print(hangman_stages[stage])



while(not game_ended):
    print("********************HANGMAN GAME*********************************************************")
    display_hangman(num_of_lives_remaining, initial_lives)
    print(f"{num_of_lives_remaining} lives remaining ************************")
    print(f"current word {"".join(array_result)}")
    guessed_word=input("Guess an alphabet \n")
    if(guessed_word not in chosen_word):
        num_of_lives_remaining=num_of_lives_remaining-1
        if(num_of_lives_remaining==0):
            game_ended=True
            display_hangman(num_of_lives_remaining, initial_lives)
            end_game(game_end_reason)
        else:
            print("You guessed the wrong character")
            print(f" number of lives remaining is {num_of_lives_remaining}")
    else:
        # print("about to get matching indices")
        matching_indices=get_matching_indices(chosen_word,guessed_word)
        # print(f" matching indices are {matching_indices}")
        for index in matching_indices:
            array_result[index]=guessed_word
            # print(f"array result {array_result}")
            # is_game_ended_check=array_result.index("_") if "_" in array_result else -1
            # if(array_result.find("_",0)==-1):
            if("_" not in array_result):
                game_ended=True
                display_hangman(num_of_lives_remaining, initial_lives)
                end_game("You guessed the correct word")











