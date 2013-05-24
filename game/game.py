
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
# Source File: game.py
# Author Name: Justin Hellsten
# Last Modified By: Justin Hellsten
# Last Modified Date: May 23, 2013
#
# Program Description: 
#
#        This game quest is called the 'Legend of the Seven Crystals'. The object of the game is
#        to pick a choice for every node (1 or 2). Which decision you can do will be described by
#        the game and all the user has to do is input 1 or 2 for the appropriate decision. There will
#        be 8 outcomes, where only 1 will be the good outcome. I hope you enjoy this game and I hope to
#        improve it more on my free time.
#
# Revision History: 
#
#         Version 0.1:
#            - display_intro() function reads from file to print introduction.
#            - world folder has been added to hold game files.
#            - get_choice() function has been implemented. This function will make it easier for coders
#              to grab the 1/2 choice from the user.
#            - All seven nodes and their corresponding check functions have been added.
#
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import time
    
def display_intro():
    introFile = open("world/intro", "r")
    print introFile.read()
    
    
def get_choice():
    userInput = raw_input()
    while userInput != '1' and userInput != '2':
        print('Invalid choice...Please pick between choice 1 and 2.')
        userInput = raw_input()
    return userInput
    
    
def nodeOne(): # 1st decision level
    print('On your left lies a path which leads to a dark and mysterious forest. On your right lies a path to what appears to be farm land. What do you do? (1 - left or 2 - right)')
    return get_choice()

def checkNodeOne(choice):
    if choice == '1':
        choice = nodeTwo()
        checkNodeTwo(choice)
    elif choice == '2':
        choice = nodeThree()
        checkNodeThree(choice)
        
        
def nodeTwo(): # 2nd decision level (left brance #1)
    print ('You approach the mysterious forest...')
    time.sleep(2)
    print ('It gets dark and spooky quickly. Trees surround you and begin to move...')
    time.sleep(2)
    print('BAM! The trees begin to awake and attack you!')
    time.sleep(2)
    print('You must act quickly! What do you do? Attack or run? (1 - Attack, 2 - Run)')
    return get_choice()

def checkNodeTwo(choice):
    if choice == '1':
        choice = nodeFour()
        checkNodeFour(choice)
    elif choice == '2':
        choice = nodeFive()
        checkNodeFive(choice)
        
        
def nodeThree():  # 2nd decision level (right brance #1)
    print('You are walking along a path that leads to a nice red brick farm...')
    time.sleep(2)
    print('You stop by a wooden gate at the end of the path and slowly creep the gate open...')
    time.sleep(2)
    print('While slowly walking towards the farm door you feel something grab you by the shoulder...')
    time.sleep(2)
    print('You turn around and see that it is the big bad wolf!')
    time.sleep(2)
    print('')

def checkNodeThree(choice):
    if choice == '1':
        print 'sdf'
    elif choice == '2':
        print 'sdf'
        
def nodeFour():
    print('The trees swings vines at you but you managed to duck in the nick of time...')
    time.sleep(2)
    print('You ready yourself to attack by lifting your fists and launch a strong upper cut at one of the trees...')
    time.sleep(2)
    print('The instance your fists and the trees bark collided you scream in pain! The punch was ineffective...')
    time.sleep(2)
    print('The trees begin to laugh at you, laugh at you so hard that they start to dissolve into ash...')
    time.sleep(2)
    print('You watch them slowly dwindle away as they all laugh insanely...')
    time.sleep(2)
    print('To your surprise out of that ash comes a fairy, with beautiful blue and gold textures...')
    time.sleep(2)
    print('It spins around and looks at you, it seems to be gesturing you to follow it deeper into the forest...')
    time.sleep(2)
    print('But just past the fairy you faintly see a cave marked with a huge skull at the entrance...')
    time.sleep(2)
    print('You wonder. What will you do? (1 - follow the fairy, 2 - go into the cave with the huge skull)')
    return get_choice()
    
def checkNodeFour(choice):
    if choice == '1':
        print 'sdf'
    elif choice == '2':
        print 'sdf'
        
def nodeFive():
    choice = ''
    while choice != '1' and choice != '2':
        print('On your left lies a path which leads to a dark and mysterious forest. On your right lies a path to what appears to be farm land. What do you do? (1 - left or 2 - right)')
        choice = raw_input()
    return choice

def checkNodeFive(choice):
    if choice == '1':
        print 'sdf'
    elif choice == '2':
        print 'sdf'
        
def nodeSix():
    choice = ''
    while choice != '1' and choice != '2':
        print('On your left lies a path which leads to a dark and mysterious forest. On your right lies a path to what appears to be farm land. What do you do? (1 - left or 2 - right)')
        choice = raw_input()
    return choice

def checkNodeSix(choice):
    if choice == '1':
        print 'sdf'
    elif choice == '2':
        print 'sdf'
        
        
def nodeSeven():
    choice = ''
    while choice != '1' and choice != '2':
        print('On your left lies a path which leads to a dark and mysterious forest. On your right lies a path to what appears to be farm land. What do you do? (1 - left or 2 - right)')
        choice = raw_input()
    return choice


def checkNodeSeven(choice):
    if choice == '1':
        print 'sdf'
    elif choice == '2':
        print 'sdf'

    
def main():

    playAgain = 'yes'
    while playAgain != 'no' and playAgain != 'n':
        
        if playAgain == 'yes' or playAgain == 'y':
            display_intro()
            
            # Actual game entry point (1st decision level)
            firstDecision = nodeOne() 
            checkNodeOne(firstDecision)
            
        print('Do you want to play again? (Yes/No, Y/N)')
        playAgain = raw_input().lower()



if __name__ == "__main__": main()
