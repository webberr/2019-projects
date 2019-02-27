import sys

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

def new_char():
	#
	sys.path('character.dat')
	print('saved')