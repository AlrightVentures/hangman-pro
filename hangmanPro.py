# Tuesday night fun - hangmanPro

# Import libraries, modules
import random
import string
from words import wordsList # wordsList is a list of random English words for the game, contains some words with dashes and spaces that are not suitable

# Check if wordsList was correctly imported
# print(wordsList)

# Some words in the list have dashes and spaces, select only a word without a dash or space 
def getValidWord(words):

    # Select a random word from the words list
    word = random.choice(words)

    # Use a while loop until the selected word doesn't contain dashes or spaces anymore
    while '-' in word or ' ' in word:
        word = random.choice(words)

    # Return randomly selected word in uppercase
    return word.upper()

# Function that runs the hangman game
def hangman():

    # Use get valid word function to select a random word from the list
    word = getValidWord(wordsList)
    # Store all unique letters from the word in a set
    letterSet = set(word) 
    # Store all alphabet letters in a set of uppercase ascii letters
    alphabet = set(string.ascii_uppercase)
    # Set storing user-guessed letters
    usedLetters = set() 
    # Store player's number of lives - reduced by 1 every time a player guesses incorrect letter
    playerLives = 5 

    # Test the game - print a word first to know what word you're looking for
    # print(word) 

    # Use while loop to keep asking player about a letter until they figure out the correct word
    # The while loop runs until they guess correctly or run out of lives
    while len(letterSet) > 0 and playerLives > 0:

        # Show player what letters they've already used 
        print("\nYou have already used letters: ", ' '.join(usedLetters))

        # Show the current word - using list comprehension
        wordDisplay = [letter if letter in usedLetters else '-' for letter in word]
        # Display a message showing correctly guessed letters and dashes for missing letters
        print("The word is: ", ' '.join(wordDisplay))

        # Ask user to pick a letter
        playerLetter = input("Type a letter you would like to choose: ").upper()

        # Check if the letter hasn't been used yet
        if playerLetter in alphabet - usedLetters:
            # Add player-selected letter to the used letters list
            usedLetters.add(playerLetter)
            # If player-selected letter is in the set of letters for the word to be guessed remove the letter from the set
            if playerLetter in letterSet:
                letterSet.remove(playerLetter)
            # If player-selected letter is not in the letter set take a way 1 life from the player
            else:
                playerLives -= 1
                print(f"There's no {playerLetter} in this word. You have {playerLives} lives left.")
        # If player-selected letter is in the set storing used letters remind user they've already used that letter
        elif playerLetter in usedLetters:
            print("Sorry! You've already used that letter!")
        # Tell user the character they chose is not a valid letter
        else:
            print("That's an invalid letter! Try again!")

    # Player exits while loop when they figured out the word or had zero lives left
    # If they lost all lives print a game over message
    if playerLives == 0:
        print("Sorry, you're dead. Game over. Sad face emoji would look good here, right?")
    # If they still have lives print a congratulations message
    else:
        print(f"Well done! You've guessed the word: {word}.")

# Play the game and enjoy!
hangman()


# Made with love.
# Check out Harry Mack on YouTube. 
# Have a great day.