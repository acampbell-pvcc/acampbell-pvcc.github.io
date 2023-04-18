# Name: Alexus Campbell
# Program Purpose: Pordle (PVCC Wordle): Word Guessing Game
#   The program chooses a random word froma  file of words. The user tries to
#   figure out the word in the fewest guess by guessing letters in the word.
#   This program uses an input FILE, LISTS, and STRING SLICES (section of the string)

import random
wordList = []
inFile = "animals.txt"
global wordFile

def main():
    global wordList
    wordFile = open(inFile, "r") #open the file for READ
    for textLine in wordFile: #read in a line of text from the file
        for word in textLine.split(): #split the line of text into words
            wordList.append(word) #add each word to the word list
    wordFile.close()

    playAgain = True
    while playAgain:
        printHeadings()
        playGame()
        yesno = input("Would you like to play again? (Y/N)")
        if yesno == "n" or yesno == "N":
            playAgain = False;
            print("Thank you for playing PORDLE!")
            return()

def printHeadings():
    print("\nWelcome to PORDLE! The PVCC Wordle Game")
    print("I will think of a word and you try to guess the letters in the word.")
    print("The number of dashes indicates the number of letters in the word.")
    print("\nGet ready for a new word...")

def playGame():
    numguess = 1
    lettersUsed = []

    wordChosen = random.choice(wordList)
    pordle = wordChosen
    for i in range (len(pordle)):
        pordle = pordle[0:i] + "_" + pordle[i+1:] #Use SLICE to replace each letter with a '_'
    print( " ".join(pordle)) #the "join" will put a space between each underscore

    while pordle != wordChosen: #keep asking the player until player guesses the word
        letterGuess = input("Please enter a letter:")
        letterGuess = letterGuess.lower()
        lettersUsed.append(letterGuess) #Add the players' letter to the list of guessed letters
        print("Number of guesses:" + str(numguess))

        for i in range(len(wordChosen)): #Search through the letters to find a match
            if wordChosen[i] == letterGuess:
                pordle = pordle[0:i] + letterGuess + pordle[i+1:]

        print("Used letters: ")
        print(lettersUsed)
        print(" ".join(pordle)) #Print the string with guessed letters with spaces in between
        numguess += 1

    print("Well done! You guessed it" + str(numguesses-1) + "guesses!")

main()
