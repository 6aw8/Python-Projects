import time
import random

print('''Welcome to Rock, Paper & Scissor game!''')

while True:
    print(' ')

    bot_choices = ['rock', 'paper', 'scissor']
    bot_choice = random.choice(bot_choices) 

    
    option = input("Please enter your option (rock, paper, or scissor): ").lower() 

    if option == bot_choice:
        print("It's a tie!")
    elif (option == 'rock' and bot_choice == 'scissor') or \
            (option == 'paper' and bot_choice == 'rock') or \
            (option == 'scissor' and bot_choice == 'paper'):
        print("You Won!")
    else:
        print("You Lost by default. Please choose a valid option!")

    play_again = input("Play again? (yes/no): ").lower()
    if play_again != 'yes':
        break  

print("Thanks for playing!")
