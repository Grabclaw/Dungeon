class Powers:

    powers = {
        "attack" : attack
    }
    
    def use_Power(self, power):
        self.powers[power](self)
    
    def attack(self):
        print("used attack!")