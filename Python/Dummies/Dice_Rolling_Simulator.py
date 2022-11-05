#Activity 2

import random
from sys import exit

computer_score = 0
your_score = 0
rounds = 0

        
def display_scores(your_score, computer_score):
    print("\n_______________________\nScores:\n_______________________\n")
    print(f"Player_score: {your_score}")
    print(f"Computer_score: {computer_score}")   
    
for i in range(5):
    print(f"\n=======================\nRound{rounds + 1}\n=======================\n")
    
    user_dice1 = random.randint(1, 6)
    print(f"player_dice1: {user_dice1}")
    user_dice2 = random.randint (1, 6)
    print(f"player_dice2: {user_dice2}")
    
    while (user_dice1 == user_dice2):
        user_dice1 = random.randint(1, 6)
        print(f"player_dice1: {user_dice1}")
        user_dice2 = random.randint (1, 6)
        print(f"player_dice2: {user_dice2}")
    
    ai_dice1 = random.randint(1, 6)
    print(f"computer_dice1: {ai_dice1}")
    ai_dice2 = random.randint(1, 6)
    print(f"computer_dice2: {ai_dice2}")
        
    while (ai_dice1 == ai_dice2):
        ai_dice1 = random.randint(1, 6)
        print(f"computer_dice1: {ai_dice1}")
        ai_dice2 = random.randint(1, 6)
        print(f"computer_dice2: {ai_dice2}")
    
    user_total = user_dice1 + user_dice2
    ai_total = ai_dice1 + ai_dice2
    
    if (user_total > ai_total):
        your_score += 1
        
    elif (ai_total > user_total):
        computer_score += 1
 
    display_scores(your_score, computer_score)
    
    if (your_score == 3):
        print("\n-----------------------\nPlayer has won!\n-----------------------\n")
        exit()
    
    elif (computer_score == 3):
        print("\n-----------------------\nComputer has won!\n-----------------------\n")
        exit()
        
    rounds += 1
    
    if (rounds == 5):
        print()
        print("-----------------------")
        print(f"Player total_score: {your_score}")
        print(f"Computer total_score: {computer_score}")
        print("-----------------------")
        
        if (your_score > computer_score):
            print("\n-----------------------\nPlayer has won!\n-----------------------\n")
        elif (computer_score > your_score):
            print("\n-----------------------\nComputer has won!\n-----------------------\n")
        elif (your_score == computer_score):
            print("\n-----------------------\nDraw!\n-----------------------\n")
        exit()
     