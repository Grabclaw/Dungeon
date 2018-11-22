#-----------------------------------------------#
# 	GameConceptNodeClass_Battle | GCNC_Battle	#
# 	Currently Connected to 0 Nodes.           	#
# 	Nodes Connected to: [None]                	#
#-----------------------------------------------#


import random as r


# This node represents the combat environment for the rogue-like game 
# with working title "Dungeon".
#
# In order to be unit tested as a node, all components required for 
# combat are roughly simulated.



class GCNC_Battle():
	def __init__(self, intMode):
		# Modes:
		# 	0 = Testing Mode.
		#	1 = Real Combat.
		
		self.INT_MODE_TESTING_MODE = 0
		self.INT_MODE_REAL_COMBAT = 1
		
		self.intMode = intMode
		
		
		# Holds function calls to all combat abilites.
		self.dictAbilities = {
			"Attack": self.mthdVoid_attack,
			"Heal": self.mthdVoid_heal
		}
		
		
		# Combatant ID's:
		# 0: Player
		# 1: Foe

		self.STATIC_INT_PLAYER = 0
		self.STATIC_INT_FOE = 1
		
		# Holds both combatants.
		self.listInstsCombatants = []


		if self.intMode == self.INT_MODE_TESTING_MODE:
			# Create sim Player 'instance':
			self.listInstsCombatants.append(
				{
					"strName": "Sim_Player",
					"intTargetID": 0,
					"intCurrentLife": 10,
					"intMaxLife": 10,
					"intHitChance": 60,
					"intPower": 2,
					"intDefense": 1,
					"intSpeed": 1,
					"listStringAbilities": ["Attack", "Heal"],
					"boolAlive": True
				}
			)

			# Create sim Monster 'instance':
			self.listInstsCombatants.append(
				{
					"strName": "Sim_Monster",
					"intTargetID": 0,
					"intCurrentLife": 10,
					"intMaxLife": 10,
					"intHitChance": 60,
					"intPower": 2,
					"intDefense": 1,
					"intSpeed": 1,
					"listStringAbilities": ["Attack"],
					"boolAlive": True
				}
			)
			
			self.mthdVoid_start()
		
		elif intMode == self.INT_MODE_REAL_COMBAT:
			print("Mode 1 not yet implemented!")
			return



	# Utiltiy Methods for combat rolls:
	def mthdBool_check_roll_within_range(self, roll, targetRange):
		if roll <= targetRange:
			boolResult = True
		else:
			boolResult = False

		return boolResult


	# Utility Methids for combat:
	def mthdVoid_apply_damage_to_target(self, instTarget, intDamage):
		if instTarget["intCurrentLife"] - intDamage > 0:
			instTarget["intCurrentLife"] -= intDamage
			
			print("| "+instTarget["strName"]+" takes " \
			+ str(intDamage)+" damage!")
			
		else:
			instTarget["intCurrentLife"] = 0
			instTarget["boolAlive"] = False
			
			print("| "+instTarget["strName"]+" has been slain!")
	
	def mthdVoid_apply_healing_to_target(self, instTarget, intHealing):
		if instTarget["intCurrentLife"] + intHealing <= instTarget["intMaxLife"]:
			instTarget["intCurrentLife"] += intHealing
			
			print("| "+instTarget["strName"]+" recovers " \
			+ str(intHealing) + \
			" life!")
			
		else:
			print("| "+instTarget["strName"]+" recovers " \
			+ str(instTarget["intMaxLife"] - instTarget["intCurrentLife"] ) \
			+" life!")
			
			instTarget["intCurrentLife"] = instTarget["intMaxLife"]

	
	# Combat Ability Methods:
	def mthdVoid_attack(self, instUser, instTarget):
		# A basic attack available to almost any dictCombatant.
		
		print("| "+instUser["strName"]+" uses Attack!")
		
		
		# (
		#   Roll \
		#   , Range
		# )
		boolHitRollResult = self.mthdBool_check_roll_within_range \
		(
			r.randint(1, 100) \
			, instUser["intHitChance"]
		)


		# Ability Hit:
		if boolHitRollResult == True:
			print("| The ability hit!")
			
			intDamage = r.randint(1, instUser["intPower"])
			intDamageAfterDefense = intDamage \
			- r.randint(0, instTarget["intDefense"])
			
			
			if intDamageAfterDefense > 0:
				self.mthdVoid_apply_damage_to_target \
				(instTarget, intDamageAfterDefense)
				
			else:
				print("| The ability failed to deal damage!")
				
		else:
			print("| The ability missed!")
		
		
		print()
		print()
	
	def mthdVoid_heal(self, instUser, instTarget):
		# A basic heal.
		
		print("| "+instUser["strName"]+" casts Heal!")
		
		intHealing = r.randint(1, instUser["intPower"])
		self.mthdVoid_apply_healing_to_target(instUser, intHealing)


		print()
		print()
	
	
	
	# Combat Game Logic
	def mthdVoid_start(self):
		print("****************")
		print("*              *")
		print("* Battle Start *")
		print("*              *")
		print("****************")
		print()
		print()
		
		print("| A " +self.listInstsCombatants[self.STATIC_INT_FOE]["strName"]+" has appeared!")

		# Get player input:
		boolGettingInput = True
		
		while boolGettingInput == True:
			print("| What would you like to do?")
			print()
			print()
			
			print("| 0 )--> Fight")
			print()
			print()
			
			strUserInput = input("| Input <==( ")
			print()
			print()

			# Fight:
			if strUserInput == "0":
				boolBattle = True
				boolGettingInput = False

			# Invalid Input:
			else:
				print("| Invalid Input")


		# React to player input:
		if boolBattle == True:
			# Combat Start:
			print("****************")
			print("*              *")
			print("* Combat Start *")
			print("*              *")
			print("****************")
			print()
			print()

			instPlayer = self.listInstsCombatants[self.STATIC_INT_PLAYER]
			instFoe = self.listInstsCombatants[self.STATIC_INT_FOE]


			# Combat Loop:
			while boolBattle == True:
				
				print("| Life: " + str(instPlayer["intCurrentLife"]) + " / " + str(instPlayer["intMaxLife"]))
				print("|")
				print("| What would you like to do?")
				print()
				print()
				
				
				for move in range(len(instPlayer["listStringAbilities"])):
					print("| "+str(move)+" )--> " + instPlayer["listStringAbilities"][move])
				print()
				print()
				
				strUserInput = input("| Input <==( ")
				print()
				print()
				
				
				# Player goes first:
				if instPlayer["intSpeed"] > instFoe["intSpeed"]:
					self.dictAbilities[instPlayer["listStringAbilities"][int(strUserInput)]] \
					(instPlayer, instFoe)
					

					if instFoe["boolAlive"] == True:
						self.dictAbilities[instFoe["listStringAbilities"][r.randrange(len(instFoe["listStringAbilities"]))]]\
						(instFoe, instPlayer)
					
					else:
						boolBattle = False
				
				
				# Speed tie:
				elif instPlayer["intSpeed"] == instFoe["intSpeed"]:
					if r.randrange(2) == 0:
						self.dictAbilities[instPlayer["listStringAbilities"][int(strUserInput)]] \
						(instPlayer, instFoe)
						
						
						if instFoe["boolAlive"] == True:
							self.dictAbilities[instFoe["listStringAbilities"][r.randrange(len(instFoe["listStringAbilities"]))]] \
							(instFoe, instPlayer)
							
						else:
							boolBattle = False
							
					else:
						self.dictAbilities[instFoe["listStringAbilities"][r.randrange(len(instFoe["listStringAbilities"]))]] \
						(instFoe, instPlayer)
						
						
						if instPlayer["boolAlive"] == True:
							self.dictAbilities[instPlayer["listStringAbilities"][int(strUserInput)]] \
							(instPlayer, instFoe)
							
						else:
							boolBattle = False
				
				
				# Foe goes first:	
				else:
					self.dictAbilities[instFoe["listStringAbilities"][r.randrange(len(instFoe["listStringAbilities"]))]] \
					(instFoe, instPlayer)
					
					
					if instPlayer["boolAlive"] == True:
						self.dictAbilities[instPlayer["listStringAbilities"][int(strUserInput)]] \
						(instPlayer, instFoe)
						
					else:
						boolBattle = False


				# Check to see if combat will continue:
				if instPlayer["boolAlive"] == False and instFoe["boolAlive"] == False:
					boolBattle = False
					print("| Combat is over: All factions were wiped out!")
					print()
					print()
				
				elif instPlayer["boolAlive"] == False or instFoe["boolAlive"] == False:
					boolBattle = False
					print("| Combat is over!")
					
					if instFoe["boolAlive"] == False:
						print("| You have won!")
						print()
						print()
					
					else:
						print("| You have died!")
						print()
						print()

		else:
			print()
			print("Error: boolBattle is false, this should not be possible")
				
			print("after getting player input!")
			print()



#Node testing code:
def funcVoid_testThisNode():
	print("|---{ Testing node: 'GCNC_Battle' }---|")
	print()
	print()

	STATIC_INT_DEMO_MODE = 0
	instanceBattle = GCNC_Battle(STATIC_INT_DEMO_MODE)

	print("|---{ Update on: | Testing node: 'GCNC_Battle' | }---|")
	print("|---{ node: 'GCNC_Battle' test was successful!   }---|")
	print()
	print()
	
	strUserInput = input("Enter any input to close this unit test | Input: ")
		
	print()
	print()
funcVoid_testThisNode()
