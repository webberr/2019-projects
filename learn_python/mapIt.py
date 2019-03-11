# This is what your program does:
# Gets a street address from the command line arguments or clipboard.
# Opens the web browser to the Google Maps page for the address.
# This means your code will need to do the following:
# Read the command line arguments from sys.argv.
# Read the clipboard contents.
# Call the webbrowser.open() function to open the web browser.

#! python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])

else:
    # Get address from clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)

