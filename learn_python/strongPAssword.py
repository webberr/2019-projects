#! python3 
import re

def strongPass(password):
    # must be greater than 8 chars
    if(len(password) < 8):
        return False
    
    # must contain upper and lower chars
    if(password.search([a-z]|[A-z]) == None):
        return False

password = 'abc123bca'
if(strongPass(password)):
    print(password + ' is Strong')
else:
    print(password + ' is not Strong')