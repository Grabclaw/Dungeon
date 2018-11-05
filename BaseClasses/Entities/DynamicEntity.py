import BaseClasses.Entities.Entity as E

class DynamicEntity(E.Entity):
      
    params = ["meta", "location"]
    
    
    def __init__(self, name, _id, x, y):
        
        E.Entity.__init__(self, name, _id)
    
        self.location = {
            "x": x,
            "y": y
        }
    
    
    
    def get_location(self, cordinate):
        return self.location[cordinate]
        
    def set_location(self, cordinate, value):
        self.location[cordinate] = value