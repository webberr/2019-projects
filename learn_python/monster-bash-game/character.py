import os
import ast

character = {
	'name':"",
	'level':0,
	'health':100,
	'damage':1,
	'armor': {
		'head':{},
		'chest':{},
		'shoulders':{},
		'hands': {},
		'legs':{},
		'feet':{}
	},
	'weapon':[],
	'inventory': {
		'rusty knife':1,
		'berries':5,
		'meat':5,
		'basic trap':5
	}
}

def showInv():
	return str(character['inventory'])

def useInv(item):
	print(item)

def showHealth():
	return str(character['health'])
	
def showLevel():
	return str(character['level'])

def newChar(name):
	# Create a new character loading the character dictionary, and save to a dat file
	charFile = open('character.dat', 'w+')
	character['name'] = name
	charFile.write(str(character))
	print('saved')
	charFile.close()
	return character

def loadChar():
	# Open a file, and save the values into a character dictionary that will be used in the program
	datFile = open('character.dat', 'r')
	content = datFile.read()
	return ast.literal_eval(content)