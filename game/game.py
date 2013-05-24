
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
#
#        Version 0.2:
#           - Added time constant to make it easy to change the wait time between print statements
#           - Set time constant for print statements to 1 seconds
#           - Implemented all scenarios 
#           - Added all outcomes
#           - For Outcome #2 added 'Dearest Helena' note using helena file.
#
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import time
    
# CONSTANTS
WAIT_TIME = 1

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
        
        
def nodeTwo(): # 2nd decision level (left branch node #1)
    print ('You approach the mysterious forest...')
    time.sleep(WAIT_TIME)
    print ('It gets dark and spooky quickly. Trees surround you and begin to move...')
    time.sleep(WAIT_TIME)
    print('BAM! The trees begin to awake and attack you!')
    time.sleep(WAIT_TIME)
    print('You must act quickly! What do you do? Attack or run? (1 - Attack, 2 - Run)')
    return get_choice()

def checkNodeTwo(choice):
    if choice == '1':
        choice = nodeFour()
        checkNodeFour(choice)
    elif choice == '2':
        choice = nodeFive()
        checkNodeFive(choice)
        
        
def nodeThree():  # 2nd decision level (right branch node #1)
    print('You are walking along a path that leads to a nice red brick farm...')
    time.sleep(WAIT_TIME)
    print('You stop by a wooden gate at the end of the path and slowly creep the gate open...')
    time.sleep(WAIT_TIME)
    print('While slowly walking towards the farm door you feel something grab you by the shoulder...')
    time.sleep(WAIT_TIME)
    print('You turn around and see that it is the big bad wolf!')
    time.sleep(WAIT_TIME)
    print('You immediately back away and grab a stick that lied on the ground...')
    time.sleep(WAIT_TIME)
    print('You must act quickly! Do you defend yourself with a stick or do you run away? (1 - Defend, 2 - Run away) ')
    return get_choice()


def checkNodeThree(choice):
    if choice == '1':
        choice = nodeSix()
        checkNodeSix(choice)
    elif choice == '2':
        choice = nodeSeven()
        checkNodeSeven(choice)

        
def nodeFour(): # 3rd decision level (left branch node #2)
    print('The trees swings vines at you but you managed to duck in the nick of time...')
    time.sleep(WAIT_TIME)
    print('You ready yourself to attack by lifting your fists and launch a strong upper cut at one of the trees...')
    time.sleep(WAIT_TIME)
    print('The instance your fists and the trees bark collided you scream in pain! The punch was ineffective...')
    time.sleep(WAIT_TIME)
    print('The trees begin to laugh at you, laugh at you so hard that they start to dissolve into ash...')
    time.sleep(WAIT_TIME)
    print('You watch them slowly dwindle away as they all laugh insanely...')
    time.sleep(WAIT_TIME)
    print('To your surprise out of that ash comes a fairy, with beautiful blue and gold textures...')
    time.sleep(WAIT_TIME)
    print('It spins around and looks at you, it seems to be gesturing you to follow it deeper into the forest...')
    time.sleep(WAIT_TIME)
    print('But just past the fairy you faintly see a cave marked with a huge skull at the entrance...')
    time.sleep(WAIT_TIME)
    print('You wonder. What will you do? (1 - follow the fairy, 2 - go into the cave with the huge skull)')
    return get_choice()
    
def checkNodeFour(choice):
    if choice == '1': # Outcome #1 - Bad Ending!
        print('You follow the fairy all the way deep into the forest and you reach an open area...')
        time.sleep(WAIT_TIME)
        print('In the center of the open area lies a giant oak tree with an old mans face imprinted on it...')
        time.sleep(WAIT_TIME)
        print('The fairy who guided you flew past you and went down the wide open mouth of the oak tree...')
        time.sleep(WAIT_TIME)
        print('You follow the fairy into the oak tree but slowly stop because it is too dark to continue further...')
        time.sleep(WAIT_TIME)
        print('Before you could do anything you hear the mouth of the tree slowly creep shut...')
        time.sleep(WAIT_TIME)
        print('You quickly run back to the exit but the mouth closes shut before you can get there...')
        time.sleep(WAIT_TIME)
        print('You begin to feel your body start floating and begin to drag further into the tree...')
        time.sleep(WAIT_TIME)
        print('After a while of being dragged you notice you can no longer feel or sense anything...')
        time.sleep(WAIT_TIME)
        print("In just a couple of moments you hear an old wizard's voice echo inside your head. It is non other than Evil Wizard Madnep!")
        time.sleep(WAIT_TIME)
        print('"They will all be mine in the end! No one shall ever dispute my rule again... - Evil Wizard Madnep"')
        time.sleep(WAIT_TIME)
        print('Game Over! You were consumed by darkness!')
    elif choice == '2': # Outcome #2 - Bad Ending!
        print('You walk closer to the cave and realize that the skull is made out of iron!')
        time.sleep(WAIT_TIME)
        print('You decide to go inside and notice that the ceiling is covered with glow in the dark mushrooms...')
        time.sleep(WAIT_TIME)
        print('After walking for a couple of minutes the glow in the dark mushrooms stop and you reach what you could only sense is a cliff')
        time.sleep(WAIT_TIME)
        print('You try to carefully peer into the darkness but lose your balance and begin to fall into the dark abyss...')
        time.sleep(WAIT_TIME)
        print('To your shock you survived the fall, and for some unknown reason have landed safely back on your feet...')
        time.sleep(WAIT_TIME)
        print('Trying to adjust to the darkness you finally begin to see a faint flashing light and begin to walk towards it...')
        time.sleep(WAIT_TIME)
        print('Getting closer you discover that it is a large treasure chest, beaconing a magnificent light just across an underground lake...')
        time.sleep(WAIT_TIME)
        print('Unable to determine how to cross the water quickly the ground begins to shake and the water starts to bubble...')
        time.sleep(WAIT_TIME)
        print('Magically out of lake in front of you a bridge slowly appears and gives you a path straight to the treasure in the middle of the lake...')
        time.sleep(WAIT_TIME)
        print('You go to the treasure chest and open it but are quickly overwhelmed and consumed by bright white light inside the chest...')
        time.sleep(WAIT_TIME)
        print('All you can see and sense now is whiteness...')
        time.sleep(WAIT_TIME)
        print('Voices begin to chant...')
        time.sleep(WAIT_TIME)
        helenaFile = open("world/helena", "r")
        print helenaFile.read()
        print('Game Over! You were consumed by whiteness!')
        
def nodeFive():
    print('You ran as fast as you can. So fast and so far you trip on a stump...')
    time.sleep(WAIT_TIME)
    print('You lose consciousness and start to dream...')
    time.sleep(WAIT_TIME)
    print('In your dream you are inside a cage being carried by an ogre...')
    time.sleep(WAIT_TIME)
    print('You watch as he carries you slowly into what appears to be a torture area with lava. You begin to panic!')
    time.sleep(WAIT_TIME)
    print('While frantically trying to find a way to escape you notice that the lock of the cage is not actually locked!')
    time.sleep(WAIT_TIME)
    print('The orgre is not paying much attention and can not see you since he is carrying you on his back...')
    time.sleep(WAIT_TIME)
    print('However you are still in a panic and you are hesitant to escape the cage...')
    time.sleep(WAIT_TIME)
    print('What do you do? Escape the cage or chicken out? (1 - Escape, 2 - Chicken ("bock,bock,bock,bock,bock,begowwwwk")')
    return get_choice()


def checkNodeFive(choice):
    if choice == '1': # Outcome #3 - Bad Ending!
        print('You quietly open the cage door and get on the ground...')
        time.sleep(WAIT_TIME)
        print('You tip toe away from the ogre as he goes in the other direction...')
        time.sleep(WAIT_TIME)
        print('However as you are tip toe away your feet get stuck in mud...')
        time.sleep(WAIT_TIME)
        print("You try to get out of the it but you can't, and soon you begin to sink into the mud...")
        time.sleep(WAIT_TIME)
        print('You sink so fast you have no time to react and you get consumed by the mud...')
        time.sleep(WAIT_TIME)
        print("Because you can't breath you die of suffocation")
        time.sleep(WAIT_TIME)
        print('Game Over! You were consumed in mud. ')
    elif choice == '2': # Outcome #4 - Bad Ending!
        print('You stayed in the cage and watched as the ogre continued carrying you to the torture/lava area...')
        time.sleep(WAIT_TIME)
        print('However suddenly the ogre places you down and says "Screw it I am hungry!"')
        time.sleep(WAIT_TIME)
        print('He puts the cage down and opens the door...')
        time.sleep(WAIT_TIME)
        print("He reaches into the cage and grabs you waist wide...")
        time.sleep(WAIT_TIME)
        print('He then lifts you up towards your mouth and swallows you whole..."')
        time.sleep(WAIT_TIME)
        print('Game Over! You were swallowed whole by the ogre!')
 
        
def nodeSix():
    print('The big bad wolf comes towards you...')
    time.sleep(WAIT_TIME)
    print('You bring up your stick and use it for your defence...')
    time.sleep(WAIT_TIME)
    print('You hold the stick high ready to swing and feel a breeze...')
    time.sleep(WAIT_TIME)
    print('When you swing the stick down towards the big bad wolf the stick instantly transformers into the legendary sword of the seven crystals!')
    time.sleep(WAIT_TIME)
    print('The big bad wolf is instantly sliced in two. You pull your sword in front of you in awe.')
    time.sleep(WAIT_TIME)
    print('Confident in yourself you walk over the dead beast into the farm house...')
    time.sleep(WAIT_TIME)
    print('Inside you notice that all the furniture are made out of candy!')
    time.sleep(WAIT_TIME)
    print('You search the house for anything useful, stopping by in a room which had two strange kind of pink candy on a table...')
    time.sleep(WAIT_TIME)
    print('Written on the first candy it says "Eat me!". Written on the second candy it says "Do not eat me!"')
    time.sleep(WAIT_TIME)
    print('You starve for candy so you decide to eat either one regardless of what they say. This is due to your confidence.')
    time.sleep(WAIT_TIME)
    print('Which one do you eat? (1 - "Eat Me!" Candy, 2 - "Do not eat me!" Candy).')
        

def checkNodeSix(choice):
    if choice == '1': # Outcome #5 - Bad ending!
        print('You pick up the "Eat Me!" candy and unwrap it...')
        time.sleep(WAIT_TIME)
        print('You put it in your mouth and start to chew...')
        time.sleep(WAIT_TIME)
        print('You notice that it taste very strange and you start to feel your heart get faster and faster!')
        time.sleep(WAIT_TIME)
        print('In a matter of seconds you drop on the floor because you feel like your chest is about to burst!')
        time.sleep(WAIT_TIME)
        print('You scream in pain clutching your head and then...')
        time.sleep(WAIT_TIME)
        print('BANG! Your chest exploded and out comes your heart...')
        time.sleep(WAIT_TIME)
        print("Game over! Your heart couldn't handle the sugar!")        
    elif choice == '2': # Outcome #6 - Good ending!
        print('You pick up the "Do not eat Me!" candy and unwrap it...')
        time.sleep(WAIT_TIME)
        print('You put it in your mouth and start to chew...')
        time.sleep(WAIT_TIME)
        print('You notice that it taste really good! And you start to feel your heart get faster and faster!')
        time.sleep(WAIT_TIME)
        print('In a matter of seconds you drop on the floor because you feel like your chest is about to burst!')
        time.sleep(WAIT_TIME)
        print('You scream in pain clutching your head and then...')
        time.sleep(WAIT_TIME)
        print('BANG! Your body is flowing with energy. So much energy you become a ball of energy!...')
        time.sleep(WAIT_TIME)
        print("You feel the amazing power as your energy transformed body flies through the house and throughout the land!")    
        time.sleep(WAIT_TIME)
        print('After about a minute of traveling you transform back into your original self...')
        time.sleep(WAIT_TIME)
        print('You scan your surroundings and see that you are in some kind of chamber...')
        time.sleep(WAIT_TIME)
        print('You look up and...behold it is the seven crystals floating in the air emiting light and energy!')
        time.sleep(WAIT_TIME)
        print('You take one step closer and hear the crystals speak!')
        time.sleep(WAIT_TIME)
        print('"Thank you dear adventurer...For awaken us from our sleep and bringing us back into order. The moment you')
        print('ate that candy the Evil Wizard Madnep spell has been broken and we risen from our long slumber. You will be')
        print('greatly awarded for your courage!"' )
        time.sleep(WAIT_TIME)
        print('You won the game! Thank you for playing!')
        
def nodeSeven():
    print('You decide to flee from the big bad wolf and run over the farm house fence into the hills beyond...')
    time.sleep(WAIT_TIME)
    print('You continue running but the sky begins to get dark and static...')
    time.sleep(WAIT_TIME)
    print('It begins to pour rain and thunder bolts rapidly hit the landscape...')
    time.sleep(WAIT_TIME)
    print('You stop in your tracks. The sky loudly ruptures!')
    time.sleep(WAIT_TIME)
    print('YOU')
    time.sleep(WAIT_TIME)
    print('SHALL')
    time.sleep(WAIT_TIME)
    print('NOT')
    time.sleep(WAIT_TIME)
    print('PASS!')
    time.sleep(WAIT_TIME)

    
def checkNodeSeven(choice):
    if choice == '1':
        print('You decide to pass through anyway and you feel the air getting static...')
        time.sleep(WAIT_TIME)
        print('You look up and see a light start to form above you...')
        time.sleep(WAIT_TIME)
        print('Electricity flashes down towards you and you get hit by it...')
        time.sleep(WAIT_TIME)
        print('You get electrocuted and your corpse is left burning!')
        time.sleep(WAIT_TIME)
        print('Game over! You did not pass...')
    elif choice == '2':
        print('You decide not to pass and head back the way you came...')
        time.sleep(WAIT_TIME)
        print('As you turn around your heart races and you see Gandalf the Grey!')
        time.sleep(WAIT_TIME)
        print('"So be it!" he yells.')
        time.sleep(WAIT_TIME)
        print('He lifts his staff and points it towards you...')
        time.sleep(WAIT_TIME)
        print('You can not move! You look at your feet and see that slowly but surely your body turning into stone.')
        time.sleep(WAIT_TIME)
        print('You yell for forgiveness but are quickly cut off as your whole body turns grey as stone...')
        time.sleep(WAIT_TIME)
        print('Game over! You got Gandalf the Greyed!')
        
        
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
