import os
import character

def start_game():
    #

def main():
    if os.path.exists('character.dat'):
        start_game(os.open(character.dat))
    else:
        new_char()

if __name__ == '__main__':
    main()
