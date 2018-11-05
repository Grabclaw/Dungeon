import BaseClasses.Entities.CombatEntity as CE

class Player(CE.CombatEntity):
	
	def __init__(self, name, _id, x, y):
		
		CE.CombatEntity.__init__(self, name, _id, x, y)
	
	
	def show_Character_Details(self):
		print()
		print()
		print("_____________________")
		print("|                   |")
		print("| Character Details |")
		print("|___________________|")
		print()
		print("| Name ) " + self.meta['name'])
		print()
		print("| LIFE ) " + str(self.stats['currentLife']))
		print("| MLFE ) " + str(self.stats['maxLife']))
		print()
		print("| HIT ) " + str(self.stats['hit']) + "%")
		print("| POW ) " + str(self.stats['power']))
		print("| DEF ) " + str(self.stats['defense']))
		print()
		print("| SPD  ) " + str(self.stats['speed']))
		print()
		print()
	
	def grow_Stat(self, stat, value):
		self.stats[stat] += value
		print()
		print("| INFO | You gained " + str(value) + " " + stat + "!")
		print()