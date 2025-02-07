class Ship:

    ##AFB version
    def __init__(self, cost, hit, capacity, hp, name, priority, AFB=None):
        self.cost=cost
        self.hit=hit
        self.hp=hp
        self.capacity=capacity
        self.name=name
        self.priority=priority
        self.AFB = AFB
        
    def __str__(self):
        """Print the name and hp of the ship."""
        return(f"Ship Name: {self.name}, HP: {self.hp}")
    def __repr__(self):
        return(f"Ship Name: {self.name}, HP: {self.hp}")

# Example usage

class Fighter(Ship):
    def __init__(self):
        super().__init__(0.5, 9, -1, 1,"Fighter",1) 
    
    
class Carrier(Ship):
    def __init__(self):
        super().__init__(3, 9, 4, 1,"Carrier",2)
        
class Cruiser(Ship):
    def __init__(self):
        super().__init__(2, 7, 0, 1,"Cruiser",3)
                
        
class Destroyer(Ship):
    def __init__(self):
        super().__init__(1, 9, 0, 1,"Destroyer",4,[9,9])
        
    def AFBarrage(self): #9x2 hits only fighters
        print("TODO")
        
class Dreadnaught(Ship):
    def __init__(self):
        super().__init__(4, 5, 1, 2,"Dreadnaught",5)
                
           
        
class Warsun(Ship):
    def __init__(self):
        super().__init__(12, [3,3,3], 6, 2,"Warsun",6)
                
                
#class Flagship(Ship): ##TODO They are all different
#    def __init__(self):
#        super().__init__(8, [7,7], 1, 2)
        
                