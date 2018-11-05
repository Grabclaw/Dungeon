class EntityManager:
    
    def __init__(self):
    
        self.objects = []
        
    
    def get_Entity(self, _id):
        for x in self.objects:
            if x.get_Meta_Detail("_id") == _id:
                return x
        
        print("get_Entity | ID: "+str(_id)+" not found in list.")
        
        for x in self.objects:
            print(x.get_Meta_Detail("name"))
        
    def replace_Entity(self, _id, new):        
        for x in self.objects:
            if x.get_Meta_Detail("_id") == _id:
                x = new
                return
        
        print("replace_Entity | ID: "+str(_id)+" not found in list.")
        
        for x in self.objects:
            print(x.get_Meta_Detail("name"))