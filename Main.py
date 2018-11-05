import Classes.EntityManagers.PlayerManager as PM
import Classes.EntityManagers.MonsterManager as MM
import Classes.FileManager as FM
import Classes.Battle as BT


def main():
	defaultPlayerSlot = 0
	currentSaveFile = 0
	
	playerManager = PM.PlayerManager()
	playerManager.create_Player_shell()
	
	monsterManager = MM.MonsterManager()
	monsterManager.create_Monster("Nep", 0, 0, "combat")
	
	fileManager = FM.FileManager()
	
	
	
	active = True
	
	inMainMenue = True
	inCharacterMenue = False
	
	while active:
		while inMainMenue:
			print()
			print("______________")
			print("|            |")
			print("| Main Menue |")
			print("|____________|")
			print()
			print("| 0 )--> Exit")
			print("| 1 )--> Load Game")
			print("| 2 )--> New Game")
			print()
			print()
			userInput = input("| Input <==( ")
			print()
			print()
			
			# Exit
			if userInput == "0":
				inMainMenue = False
				active = False
				
			# Load Game
			elif userInput == "1":
				player = fileManager.load_Entity(playerManager.get_Entity(defaultPlayerSlot), currentSaveFile)
				playerManager.replace_Entity(player.meta["_id"], player)
				
				inMainMenue = False
				inCharacterMenue = True
					
			# New Game
			elif userInput == "2":
				playerManager.fill_Player_Shell(defaultPlayerSlot)
				
				inMainMenue = False
				inCharacterMenue = True
		
		
		while inCharacterMenue:
			print()
			print("___________________")
			print("|            	  |")
			print("| Character Menue |")
			print("|_________________|")
			print()
			print("| 0 )--> Return To Main Menue")
			print("| 1 )--> Exit Game")
			print("| 2 )--> Character Details")
			print("| 3 )--> Save Game")
			print("| 4 )--> Start")
			print()
			print()
			userInput = input("| Input <==( ")
			print()
			print()
			
			# Return to Main Menue
			if userInput == "0":
				inCharacterMenue = False
				inMainMenue = True
			
			# Exit Game
			elif userInput == "1":
				inCharacterMenue = False
				active = False
				
			# Character Details
			elif userInput == "2":
				playerManager.get_Entity(defaultPlayerSlot).show_Character_Details()
				
			# Save Game
			elif userInput == "3":
				fileManager.save_Entity(playerManager.get_Entity(defaultPlayerSlot), currentSaveFile)
				
			# Start
			elif userInput == "4":
				monsters = []
				monsters.append(monsterManager.create_Battle_Copy(monsterManager.get_Entity(0)))
				
				BT.Battle(playerManager.get_Entity(defaultPlayerSlot), monsters).battle()
				
			
			
if __name__ == "__main__":
	main()