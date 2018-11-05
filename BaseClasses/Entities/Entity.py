class Entity:
    
    params = ["meta"]
    
    
    def __init__(self, name, _id):
        
        self.meta = {
            "name": name,
            "_id": _id
        }
    
    
    
    def get_Meta_Detail(self, detail):
        return self.meta[detail]
    
    def set_Meta_Detail(self, detail, value):
        self.meta[detail] = value