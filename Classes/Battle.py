class Battle():
    
    def __init__(self, playerBattleCopy, monsterBattleCopyList):
        self.playerBattleCopy = playerBattleCopy
        self.monsterBattleCopyList = monsterBattleCopyList
        
    
    def battle(self):
        battle = False
        
        print()
        print()
        
        for monster in self.monsterBattleCopyList:
            print("| A " +monster.get_Meta_Detail("name")+" has appeared!")
            
        print()
        print()
        print("| What would you like to do?")
        print()
        print("| 0 )--> Fight")
        print("| 1 )--> Flee")
        print()
        print()
        userInput = input("| Input <==( ")
        print()
        print()
        
        # Fight
        if userInput == "0":
            battle = True
        
        # FLee
        elif userInput == "1":
            print("| You attempt to flee!")
            print()
            print()
            
            for monster in self.monsterBattleCopyList:
                # If any of the Monster's speed roll is higher than the plyaer, the player cannot escape.
                if monster.roll_Stat_Check("speed", self.playerBattleCopy.roll_Stat("speed")):
                    print("| You cannot escape!")
                    battle = True
                    return
            
            # If the player escapes.
            print("| You get away!")
            print()
            print()
        
        # Invalid Input
        else:
            print()
            print("| Invalid Input")
            print()
        
        
        print()
        print()
        print("****************")
        print("*              *")
        print("* Combat Start *")
        print("*              *")
        print("****************")
        print()
        print()
        

        while battle:
            print()
            print()
            print("| What would you like to do?")
            print()
            print("| 0 )--> Fight")
            print("| 1 )--> Flee")
            print()
            print()
            userInput = input("| Input <==( ")
            print()
            print()
            
            return
            