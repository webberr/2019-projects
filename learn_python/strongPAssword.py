#! python3 
import re

def strongPass(password):
    # must be greater than 8 chars
    if(len(password) < 8):
        return False
    
    # must contain upper and lower chars
    if(re.search('[a-zA-Z]', password) == None):
        return False

    return True

password = 'a12345678'
if(strongPass(password)):
    print(password + ' is Strong')
else:
    print(password + ' is not Strong')