# Importing module implements pseudo-random number generation
# Importing module implements time based functions
import random
import time


"""
    -------HANGMAN-------
    Game logic:
    1. Player enters name to begin
    2. A random word will be selected from our pre-populated list of words.
    3. The player must guess the word in 6 attempts, guessing one letter at a time
    4. Incorrectly guessed letters will be displayed to Player before each guess.
    5. Before each guess a hangman drawing will be displayed based on the number of guesses left
    6. If Player guesses all letters (full word) correct in 6 attempts, Player wins
    7. If Player doesn't guess all letters (full word) correct in 6 attempts, Player loses
    8. Player granted choice to replay game.
"""
# Generating global variables
correct_letters = []
incorrect_letters = []
random_word = ""
guesses_left = 6
game_over = False

# Game logic functions

def request_player_name():
    """Ask player to enter thier Player name"""

def select_random_word():
    """Generate a randomly selected word from our predefined list of words"""

def display_blank_word():
    """Print out the word with dashes for letters that haven't been guessed yet"""

def print_hangman():
    """Print out the hangman drawing based on the number of lives left"""

def letter_validation():
    """Will make sure the user types only 1 letter that has not been used before"""

def letter_check_correct():
    """Will check if the letter guessed is correct and update global variables based on the result"""

def check_for_game_over():
    """Check to see if the player has won or lost"""

def check_for_replay():
    """Check is Player wishes to replay, else exit"""

def main():
    """The entry point of the application, will call all the other methods in a game loop"""