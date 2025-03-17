import time
import random

print('''Welcome to Rock, Paper & Scissor game!''')

while True:  # Create a loop to play multiple rounds
    print(' ')

    # Bot's choice
    bot_choices = ['rock', 'paper', 'scissor']
    bot_choice = random.choice(bot_choices)  # Choose randomly each round

    # User's choice
    option = input("Please enter your option (rock, paper, or scissor): ").lower()  # Lowercase for consistency

    # Determine the winner
    if option == bot_choice:
        print("It's a tie!")
    elif (option == 'rock' and bot_choice == 'scissor') or \
            (option == 'paper' and bot_choice == 'rock') or \
            (option == 'scissor' and bot_choice == 'paper'):
        print("You Won!")
    else:
        print("You Lost by default. Please choose a valid option!")

    # Ask if the user wants to play again
    play_again = input("Play again? (yes/no): ").lower()
    if play_again != 'yes':
        break  # Exit the loop if the user doesn't want to play again

print("Thanks for playing!")
