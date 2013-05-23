'''
Created on May 23, 2013

@author: Justin Hellsten
'''
import random
import time

# Constant Variables
TRUE = 1
FALSE = 0
FAIL = -1


def yes_no_input():
    userInput = raw_input().lower()
    if userInput == 'yes' or userInput == 'y':
        return TRUE
    elif userInput == 'no' or userInput == 'n':
        return FALSE
    else:
        print ('Could not understand input...')
        return FAIL
    
    
def display_intro():
    introFile = open("world/intro", "r")
    print introFile.read()
    
    
def nodeOne():
    landscape = ''
    while landscape != '1' and landscape != '2':
        print ('On your left lies a path which leads to a dark and mysterious forest. On your right lies a path to what appears to be farm land. What do you do? (1 - left or 2 - right)')
        landscape = raw_input()
    return landscape


def checkNodeOne(chosenLandscape):
    print chosenLandscape
    if chosenLandscape == 1:
        print ('You approach the mysterious forest...')
        time.sleep(2)
        print ('It gets dark and spooky quickly. Trees surround you and begin to move...')
        time.sleep(2)
        print ('BAM! The trees begin to awake and attack you! What do you do?')
    elif chosenLandscape == 2:
        print ('Hills')



def play_game():
    landscapeNumber = nodeOne()
    checkNodeOne(landscapeNumber) 
    
def main():

    playAgain = TRUE
    while playAgain:
        display_intro()
        play_game()
    
        playAgain = FAIL
        while playAgain == FAIL:
            print ('Do you want to play again? (yes or no)')
            playAgain = yes_no_input()


if __name__ == "__main__": main()
