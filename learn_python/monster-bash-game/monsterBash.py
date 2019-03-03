import sys
import os
import ast
import character as char
import monster
import game

def intro():
    #
    print("********************************************************")
    for i in range(2):
        print("**                                                    **")
    print("**                   Monster Bash                     **")
    for i in range(2):
        print("**                                                    **")
    print("********************************************************")
    print('\n')
    print('Press \'Q\' or \'quit\' to quit the game')
    print('Press \'inv\' to show your inventory player\'s inventory')

def main():
    gameChar = {}
    if os.path.exists('character.dat'):
        gameChar = char.loadChar()
    else:
        print("Please enter the name of your character: ")
        name = input()
        gameChar = char.newChar(name)
    
    print('Welcome ' + gameChar['name'])
    gameState = ""
    while 'quit' or 'Q' not in gameState:
        gameState = input()
        if gameState == 'inv':
            print(char.showInv())
        elif gameState.find('use'):
            char.useInv(gameState)
        elif gameState == 'quit' or 'Q':
            break

if __name__ == '__main__':
    intro()
    main()
