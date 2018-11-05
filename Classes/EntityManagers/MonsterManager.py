import BaseClasses.EntityManager as EM
import Classes.Entites.Monster as Mon

class MonsterManager(EM.EntityManager):
    
    def __init__(self):
        
        EM.EntityManager.__init__(self)
    
    
    def create_Monster(self, name, x, y, behavior):
        _id = len(self.objects)
        
        self.objects.append(Mon.Monster(name, _id, x, y, behavior))
        
    def create_Battle_Copy(self, monster):
        params = monster.get_all_params()
        return Mon.Monster(params["meta"]["name"],
                            params["meta"]["_id"],
                            params["location"]["x"], 
                            params["location"]["y"],
                            "combat")