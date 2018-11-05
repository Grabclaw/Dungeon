class FileManager:
    saveGameFolderLocation = "ExternalGameData/Saves/"
    saveGameFileNames = ["myfile.txt"]
    
    
    
    def save_Entity(self, entity, saveFile):
        print()
        print("| Attempting to save game...")
        
        f = open(self.saveGameFolderLocation + self.saveGameFileNames[saveFile], "w")
        
        for param in entity.params:
            if param == "meta":
                for detail in entity.meta.values():
                    f.write(str(detail) + "\n")
                    
            elif param  == "location":
                for detail in entity.location.values():
                    f.write(str(detail) + "\n")
                    
            elif param  == "stats":
                for stat in entity.stats.values():
                    f.write(str(stat) + "\n")
                    
        print("| The game has been saved!")
        print()
        print()
            
    def load_Entity(self, entity, saveFile):
        print()
        print("| Attempting to load game...")
        
        f = open(self.saveGameFolderLocation + self.saveGameFileNames[saveFile], "r")
        
        for param in entity.params:
            if param == "meta":
                for detail in entity.meta.keys():
                    entity.meta[detail] = f.readline().rstrip()
                    
            elif param  == "location":
                for stat in entity.location.keys():
                    entity.location[stat] = f.readline().rstrip()
                    
            elif param  == "stats":
                for stat in entity.stats.keys():
                    entity.stats[stat] = f.readline().rstrip()
                    entity.stats[stat] = int(entity.stats[stat])
                    
        entity.meta["_id"] = int(entity.meta["_id"])
        
        print("| The game has been loaded!")
        print()
        print()
        
        return entity