import os

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

def newChar(name):
	# Create a new character loading the character dictionary, and save to a dat file
	charFile = os.open("character.dat", "w+")
	character['name'] = name
	charFile.write(character)
	print('saved')

def loadChar():
	# Open a file, and save the values into a character dictionary that will be used in the program
	datFile = os.open('character.dat')
	return datFile