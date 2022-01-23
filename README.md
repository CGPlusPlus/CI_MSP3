# HANGMAN
Hangman is a Python terminal game, which runs in Code Institutes mock terminal, deployed on Heroku.

Players try to guess a randomly selected word without exceeding a given number of incorrect guesses.
If players can do it within the guess limit, they will win.

Developed by: Conor Gorman  
Live site: https://cgplusplus-hangman.herokuapp.com

## How to Play
From [Wikipedia](https://en.wikipedia.org/wiki/Hangman_(game)), Hangman is a paper and pencil guessing game for two or more players. One player thinks of a word, phrase or sentence and the other(s) tries to guess it by suggesting letters within a certain number of guesses.  

In this version of Hangman, the Player will be playing against the computer. The computer will randomly select a word, from a list of predefined words and the Player must attempt to guess this word.  
The player must do so without getting HANGMAN, which is when all incorrect guesses have been made (6 in this instance).  

The word will be printed using _ characters to represent as of yet unknown letters.  
Once a letter is guessed correct, it will be displayed alonside the _ characters.  

## Features
### Current Features
The game logic is as below:  
1.  Player runs game and is welcomed with game instructions.  
    <image src="images/intro.png">  

2.  Player is requested to enter name.  
    <image src="images/enter_name.png">  

3.  A random word will be selected from a pre-populated list of words.  These are in the words.txt file.    

4.  The base Hangman image is printed, along with the Word, represented by _ characters.  
    <image src="images/blank_word.png">  

5.  The player must guess the word,  guessing one letter at a time. The first letter is now entered by the User.  
    <image src="images/first_guess.png">  

6.  Incorrectly guessed letters will be displayed to Player before each guess. Along with a hangman drawing, again based on the number of guesses left.  
    <image src="images/incorrect_guess.png">  

7.  If Player guesses all letters correct, within 6 incorrect guesses, the Player wins.  
    <image src="images/win_game.png">

8.  Inversely, if Player doesn't guess all letters correct within 6 incorrect guesses, the Player loses.  
    <image src="images/lose_game.png">  

9.  After each game, the Player is granted choice to replay the game.  
    <image src="images/replay.png">    

### Future Features
•	Setup different word genres e.g. Animals, Films, Fruits, and display which genre the word belongs to so the Player can better judge what the answer may be. Again, the randomisation can select the genre, along with a random word from that genre.
•	Allow for guessing of full word in between guesses. Incorrect attempts may or may not be penalised as an incorrect guess.  
•	Game can have difficulty levels where either the number incorrect guesses allowed changes, or length / complexity of word may change.

## Data Model
To run this program, a script module run.py is used. This module contains all the functions for running this program.    
Within the run.py module are the classes below:  
    •	intro() - This function introduces the Player to the game logic.  
    •	request_player_name() - as the name states, this gathers the Players name.  
    •	select_random_word() - generates a randomly selected word from a predefined list of words (words.txt file).  
    •	print_hangman() - prints hangman drawing, depending on how many incorrect guesses Player has made.  
    •	display_blank_word() - prints word as blank letters (_) where not guessed yet, or letters if correctly guessed.  
    •	letter_validation() - collects letter from Player input and checks if input is a single letter between A - Z.  
    •	letter_check_correct() - determines whether Player input is contained within random word.  
    •	check_for_game_over() - As name states, checks to see if game is over (win or lose).  
    •	check_for_replay() - When game is over, checks whether Player wishes to play again or not.  
    •	main() - main execution point of program, which executes each function in correct order.  

## Testing  
Throughout the complete process I have tested the functionality in a couple of different ways:  
    •	Manually running the program in the GitPod Terminal  
    •	Passing the Python code through the PEP8 online linter, which can be found [here](http://pep8online.com)  
    •	Coding for data input validation, when input is requested by the terminal  

### Bugs  
There wasn't many bugs within my program.  
However, one did appear around an iterative statement within the letter_validation() function.  
This bug was due to a code error where not all possible outcommes were coded for, causing an infinite loop of print statements.  
The original line of code was:  
if guesses_left == 6 and len(correct_letters) == 0:  
// do something here  

This however, didn't take into consideration that guesses_left may be 5 and len(correct_letters) may be > 0.  
This possibility wasn't coded for and caused an infinite loop of prints.  
To correct this, the line of code was changed to:  
if len(correct_letters) == 0 and len(incorrect_letters) == 0:  
// do something here  

By changing to this code, the guesses_left becomes redundent, as the first guessed letter will either be right or wrong, therefore avoiding the infinite loop.  

### Remaining Bugs
There is no remaining bugs that I am aware of.

### Validator Testing
[PEP8Online](http://pep8online.com) tester was used to test the Python code contained within the run.py module.  
This returned the below, which only relates to blankspace lines:  
<image src="images/pep8.png">  

I removed these by cleaning up the blankspace:  
<image src="images/pep8_all_right.png">   

## Technologies Utilised
### Languages
•	Python 
### Tools 
•	Git  
•	Github  
•	Gitpod  
•	PEP8 Online Linter 
•	Heroku
 
## Deployment
This website was deployed using Heroku Platform following these steps:   
    •   Push the code to Github using git push.  
    •	Go to the Heroku Dashboard.  
    •	In the Heroku Dashboard, click on the Create new app button.  
    •	Enter an app name (cgplusplus-hangman) and region (Europe) and click the Create app button.  
    •	Click on settings and in the 'Config Vars' section, click on Reveal Config Vars. Add a key of PORT and a value of 8000.  
    •	In the 'Build Packs' section, click on Add Build Pack and select 'Python'. Click Save Changes button. Repeat this step again, except select 'NodeJS'.  
    •	Click on Deploy tab and choose Deployment Method - Github.  
    •	In the Connect to Github section, type MSP3 in the repo-name box and click Search button. Click the Connect button next to CGPlusPlus/CI_MSP3.  
    •	Heroku app is now connected to the Github repository. Next, navigate to the Manual deploy section, ensure the branch to deploy is main. Click on Deploy Branch button.  
    •	This app is now deployed at [CGPlusPlus-HANGMAN](https://cgplusplus-hangman.herokuapp.com)  

The repository can also be cloned by following the below steps:  
•	Navigate  to the GitHub repository  
•	Click on 'Code' at the top of the repository  
•	Select to clone either HTML, SSH or GitHub CLI  
•	Go to the working directory you wish to work from  
•	Go to Git Bash  
•	Type git clone and paste the URL from your clipboard ($ git clone https://github.com/USERNAME/REPOSITORY)  
•	Press enter to create your clone  

## Acknowledgements
### Media
•	Random Words - Although these can be any random words, I used the Random Word Generator website to generate a list of 50 words for me: https://www.randomlists.com  

### Code
•	Python Basics Project Assignment: How To Create Hangman in under 10 minutes! - This YouTube video was used as an inspiration in deciding what project to complete - https://www.youtube.com/watch?v=ynwB-QfOPRw  
