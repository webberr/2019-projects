import sys
import os
import character as char
import monster
import game

gameChar = {}

def intro():
    #
    print("********************************************************")
    for i in range(2):
        print("**                                                    **")
    print("**                   Monster Bash                     **")
    for i in range(2):
        print("**                                                    **")
    print("********************************************************")

def main():
    #
    if os.path.exists('character.dat'):
        gameChar = char.loadChar()
    else:
        print("Please enter the name of your character: ")
        name = sys.argv[0]
        gameChar = char.newChar(name)

if __name__ == '__main__':
    intro()
    main()
