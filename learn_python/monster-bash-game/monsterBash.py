import sys
import os
import character
import monster
import game

character = {}

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
        character = loadChar()
    else:
        character = newChar()

if __name__ == '__main__':
    intro()
    main()
