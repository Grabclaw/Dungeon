import random
import BaseClasses.Entities.DynamicEntity as DE

class CombatEntity(DE.DynamicEntity):
    
    params = ["meta", "location", "stats"]
    
    
    def __init__(self, name, _id, x, y):
        
        DE.DynamicEntity.__init__(self, name, _id, x, y)
    
        self.stats = {
            "currentLife": 10,
            "maxLife": 10,
            "hit": 60,
            "power": 1,
            "defense": 1,
            "speed": 1
        }
    
        self.powers = []
    
    
    
    def set_Stat(self, stat, value):
        self.stats[stat] = value
    
    
    def add_power(self, power):
        self.powers.append(power)
    
    def remove_power(self, power):
        self.powers.remove(power)
    
    
    def roll_Stat(self, stat):
        roll = random.randint(self.stats[stat], self.stats[stat] + 1)
        
        print("|" + self.meta["name"] + " Rolled:" + str(roll) + " for " + stat)
        
        return roll
        
    def roll_Stat_Check(self, stat, success_value):
        roll = random.randint(self.stats[stat], self.stats[stat] + 1)
        
        print("|" + self.meta["name"] + " Rolled: " + str(roll) + " for " + stat)
        
        if random.randint(self.stats[stat], self.stats[stat] + 1) >= success_value:
            return True
        else:
            return False
    
    
    def get_all_params(self):
        return {"meta":self.meta, 
                "location":self.location, 
                "stats":self.stats, 
                "powers":self.powers}