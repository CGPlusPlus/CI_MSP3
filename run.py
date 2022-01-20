# Importing module implements pseudo-random number generation
# Importing module implements time based functions
import random
import time


"""
    -------HANGMAN-------
    Game logic:
    1. Player enters name to begin
    2. A random word will be selected from our pre-populated list of words.
    3. The player must guess the word in 6 attempts,
        guessing one letter at a time
    4. Incorrectly guessed letters will be displayed to Player
        before each guess.
    5. Before each guess a hangman drawing will be displayed
        based on the number of guesses left
    6. If Player guesses all letters (full word) correct in 6 attempts,
        Player wins
    7. If Player doesn't guess all letters (full word) correct in 6 attempts,
        Player loses
    8. Player granted choice to replay game.
"""

# Generating global variables
correct_letters = []
incorrect_letters = []
random_word = ""
guesses_left = 6
player_name = ""
game_over = False

# Game logic functions


# Request player to enter name 
def request_player_name():
    global player_name
    
    # Input field for Player name, strip any whitespace
    player_name = input('Welcome to Hangman, please enter your Player name: ')
    player_name = player_name.strip()

    return player_name


# Generate a randomly selected word from our predefined list of words
def select_random_word():
    pass


# Print out the word with dashes for letters that haven't been guessed
def display_blank_word():
    pass


# Print out the hangman drawing based on the number of lives left
def print_hangman():
    pass


# Will make sure the user types only 1 letter that has not been used before
def letter_validation():
    pass


# Check if the letter guess is correct and update variables based on result
def letter_check_correct():
    pass


# Check to see if the player has won or lost
def check_for_game_over():
    pass


# Check is Player wishes to replay, else exit
def check_for_replay():
    pass


# Game entry point, will call all other methods in a loop
def main():
    global game_over
    
    print(" ----- Welcome to Hangman ---- ")
    request_player_name()
    select_random_word()
    
    # Start while loop for game to run while game_over = False
    while game_over is False:
        print_hangman()
        display_blank_word()

        # Print incorrect guesses before each guess
        if len(incorrect_letters) > 0:
            print("Incorrect guesses: \n"+incorrect_letters)

        letter_check_correct()
        check_for_game_over()

    # If game_over = True, check for Player replay
    if game_over:
        check_for_replay()


# Will only be called when you run the python program from the terminal
if __name__ == '__main__':
    main()
