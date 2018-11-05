import BaseClasses.EntityManager as EM
import Classes.Entites.Player as Ply



class PlayerManager(EM.EntityManager):
    
    def __init__(self):
        EM.EntityManager.__init__(self)
    
    
    def create_Player_shell(self):
        startingLocationX = 0
        startingLocationY = 0
        
        self.objects.append(Ply.Player("<PlayerHolder>", len(self.objects), startingLocationX, startingLocationY))
        
    def create_Battle_Copy(self, player):
        params = player.get_all_params()
        return Ply.Player(params["meta"]["name"],
                            params["meta"]["id"],
                            params["location"]["x"], 
                            params["location"]["y"])
    
    
    def fill_Player_Shell(self, slot):
        print()
        print("__________________________")
        print("|                        |")
        print("| Chreate your character |")
        print("|________________________|")
        print()
        print("| What is your character's name?")
        print()
        print()
        userInput = input("| Name <==( ")
        print()
        print()

        self.objects[slot].set_Meta_Detail("name", userInput)