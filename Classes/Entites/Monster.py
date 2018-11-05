import BaseClasses.Entities.CombatEntity as CE

class Monster(CE.CombatEntity):
    
    def __init__(self, name, _id, x, y, behavior):
        
        CE.CombatEntity.__init__(self, name, _id, x, y)
    
        self.powers = []
        self.behavior = behavior