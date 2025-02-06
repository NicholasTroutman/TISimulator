class Ship:
    def __init__(self, cost, hit, capacity, hp):
        self.cost=cost
        self.hit=hit
        self.hp=hp
        self.capacity=capacity

class Fighter(Ship):
    def __init__(self):
        super().__init__(0.5, 9, -1, 1) 
    
    
class Carrier(Ship):
    def __init__(self):
        super().__init__(3, 9, 4, 1)
        
class Cruiser(Ship):
    def __init__(self):
        super().__init__(2, 7, 0, 1)
                
        
class Destroyer(Ship):
    def __init__(self):
        super().__init__(1, 9, 0, 1)
        
    def AFBarrage(self): #9x2 hits only fighters
        print("TODO")
        
class Dreadnaught(Ship):
    def __init__(self):
        super().__init__(4, 5, 1, 2)
                
           
        
class Warsun(Ship):
    def __init__(self):
        super().__init__(12, [3,3,3], 6, 2)
                
                
#class Flagship(Ship): ##TODO They are all different
#    def __init__(self):
#        super().__init__(8, [7,7], 1, 2)
        
                