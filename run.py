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


# Introduction to Hangman game
def intro():
    print("Hangman is a guessing game, where a word is randomly generated")


# Request player to enter name
def request_player_name():
    global player_name
    
    # Input field for Player name, strip any whitespace
    player_name = input('Welcome to Hangman, please enter your Player name: ')
    player_name = player_name.strip().capitalize()
    print("Hi "+player_name+", let's get started...")
    return player_name


# Generate a randomly selected word from our predefined list of words
def select_random_word():
    
    global random_word
    # setup list of words variable
    words_list = []
    
    # using words.txt file populate words list line by line
    with open("./words.txt", "r") as file:
        for line in file:
            words_list.append(line.strip().upper())

    # generate random number based on current runtime
    random.seed(time.time())
    random_word = random.choice(words_list)


# Print out the hangman drawing based on the number of lives left
def print_hangman():
    global guesses_left

    if guesses_left == 6:
        print("+------------+")
        print("|            |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("+-------+")
    elif guesses_left == 5:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|")
        print("|")
        print("|")
        print("|")
        print("+-------+")  
    elif guesses_left == 4:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|            |")
        print("|")
        print("|")
        print("|")
        print("+-------+")
    elif guesses_left == 3:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|            |")
        print("|           /")
        print("|")
        print("|")
        print("+-------+")
    elif guesses_left == 2:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|            |")
        print("|           / \\")
        print("|")
        print("|")
        print("+-------+")
    elif guesses_left == 1:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|            |\\")
        print("|           / \\")
        print("|")
        print("|")
        print("+-------+")
    elif guesses_left == 0:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|           /|\\")
        print("|           / \\")
        print("|")
        print("|")
        print("+-------+")


# Print out the word with dashes for letters that haven't been guessed
def display_blank_word():
    global correct_letters
    global incorrect_letters

    # Loop through random word, print either a _ or correctly guessed letters
    for i in range(0, len(random_word)):
        letter = random_word[i]
        if letter in correct_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("")


# Will make sure the user types only 1 letter that has not been used before
def letter_validation():
    global guesses_left
    valid_letter = False
    letter = ""
    
    # Negative feedback loop
    while valid_letter is False:
        # Display input text based on guesses remaining
        if guesses_left == 6:
            letter = input("Enter first guess: ")
            letter = letter.strip().upper()
        elif guesses_left < 6:
            letter = input("Enter next guess: ")
            letter = letter.strip().upper()
        
        # Validation to check if Player input is acceptable
        if len(letter) > 1:
            print("You must enter a single letter, please try again!")
        elif len(letter) <= 0:
            print("You cannot enter no value, please try again!")
        elif letter.isalpha():
            if letter in correct_letters or letter in incorrect_letters:
                print("You have already guessed the letter " + letter +
                      ", please try again!")
            else:
                valid_letter = True

        else:
            print("Input must be a letter between A and Z, please try again!")

    return letter


# Check if the letter guess is correct and update variables based on result
def letter_check_correct():
    global correct_letters
    global incorrect_letters
    global guesses_left
    
    # Retrieve letter following validation and check it its in random_word
    letter = letter_validation()
    if letter in random_word:
        correct_letters.append(letter)
    else:
        incorrect_letters.append(letter)
        guesses_left -= 1


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
    intro()
    request_player_name()
    select_random_word()
    
    # Start while loop for game to run while game_over = False
    while game_over is False:
        print_hangman()
        display_blank_word()

        # Print incorrect guesses before each guess
        if len(incorrect_letters) > 0:
            print("\nIncorrect guesses: ")
            print(incorrect_letters)
        
        letter_check_correct()
        check_for_game_over()

    # If game_over = True, check for Player replay
    if game_over:
        check_for_replay()


# Will only be called when you run the python program from the terminal
if __name__ == '__main__':
    main()
