import os
import character
import monster
import game

def start_game():
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
        start_game(os.open('character.dat'))
    else:
        new_char()

if __name__ == '__main__':
    main()
