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
    def __init__(self, upgrade=False):
        if upgrade:
            super().__init__(0.5, 8, -1, 1,"Fighter",1)
        else:
            super().__init__(0.5, 9, -1, 1,"Fighter",1)
        
    
class Carrier(Ship):
    def __init__(self, upgrade=False):
        if upgrade:
            super().__init__(3, 9, 6, 1,"Carrier",2)
        else:
            super().__init__(3, 9, 4, 1,"Carrier",2)
            
class Cruiser(Ship):
    def __init__(self, upgrade=False):
        if upgrade:
            super().__init__(2, 3, 1, 1,"Cruiser",3)
        else:
            super().__init__(2, 7, 0, 1,"Cruiser",3)
                
        
class Destroyer(Ship):
    def __init__(self, upgrade=False):
        if upgrade:
            super().__init__(1, 8, 0, 1,"Destroyer",4,[6,6,6])
        else:
            super().__init__(1, 9, 0, 1,"Destroyer",4,[9,9])
                
class Dreadnaught(Ship):
    def __init__(self, upgrade=False):
        if upgrade:
            super().__init__(4, 5, 1, 2,"Dreadnaught",5)
        else:
            super().__init__(4, 5, 1, 2,"Dreadnaught",5)
                
           
        
class Warsun(Ship):
    def __init__(self):
        super().__init__(12, [3,3,3], 6, 2,"Warsun",7) #flagship is 6
                
                
class Flagship(Ship): ##TODO They are all different
    def __init__(self,faction):
        flagships = {
            "Arborec": [8, [7, 7], 5, 2, "Arborec Flagship", 6],
            "Barony": [8, [5, 5], 3, 2, "Barony Flagship", 6],
            "Saar": [8, [5, 5], 3, 2, "Saar Flagship", 6],
            "Muaat": [8, [5, 5], 3, 2, "Muaat Flagship", 6],
            "Hacan": [8, [7, 7], 3, 2, "Hacan Flagship", 6],  # pay 1 trade good, +1 to die roll, 1/roll. All rolls in system.
            "Sol": [8, [5, 5], 12, 2, "Sol Flagship", 6],
            "Ghost": [8, [5], 3, 2, "Ghost Flagship", 6],
            "L1Z1X": [8, [5, 5], 5, 2, "L1Z1X Flagship", 6],  # hits produced by this ship and dreadnoughts are assigned to non-fighters if able
            "Mentak": [8, [7, 7], 3, 2, "Mentak Flagship", 6],  # Other player's ship cannot use sustain damage
            "Naalu": [8, [9, 9], 6, 2, "Naalu Flagship", 6],
            "Nekro": [8, [9, 9], 3, 2, "Nekro Flagship", 6],  # Ground forces participate in space combat
            "Sardakk": [8, [6, 6], 3, 2, "Sardakk Flagship", 6],  # +1 to each ship combat in system
            "Jol-Nar": [8, [6, 6], 3, 2, "Jol-Nar Flagship", 6],  # When this ship rolls 9/10, (before mods), produce 2 additional hits
            "Winnu": [8, 7, 3, 2, "Winnu Flagship", 6],  # Roll dice equal to the # of opponent's non-fighter ships
            "Xxcha": [8, [7, 7], 3, 2, "Xxcha Flagship", 6],  # Space Cannon 5(x3), adjacent attacks
            "Yin": [8, [9, 9], 3, 2, "Yin Flagship", 6],  # When Destroyed, destroy all ships
            "Yssaril": [8, [5, 5], 3, 2, "Yssaril Flagship", 6],
            "Argent": [7, [7, 7], 3, 2, "Argent Flagship", 6],  # no space cannon against you
            "Empyrean": [8, [5, 5], 3, 2, "Empyrean Flagship", 6],  # 2 influence to repair sustain in system
            "Mahact": [8, [5, 5], 3, 2, "Mahact Flagship", 6],  # Combat against opponent whose command token is not in your fleet pool, +2 to this unit's combat rolls
            "NaazRokha": [8, [9, 9], 4, 2, "Naaz Flagship", 6],
            "Nomad": [8, [7, 7], 3, 2, "Nomad Flagship", 6],  # UPGRADE [8,[5,5],6,2,"Nomad Flagship", 6,[5,5,5]]
            "Ul": [8, [7, 7], 3, 2, "Ul Flagship", 6],
            "Cabal": [8, [5, 5], 3, 2, "Cabal Flagship", 6],
            "Keleres": [8, [7, 7], 6, 2, "Keleres Flagship", 6]
        }
        f = flagships[faction]
        
        if len(f)==6: #Base
            super().__init__(f[0],f[1],f[2],f[3],f[4],f[5])
        if len(f)==7: #AFB
            super().__init__(f[0],f[1],f[2],f[3],f[4],f[5],f[6])
                