class Ship:

    ##AFB version
    def __init__(self, cost, hit, capacity, hp, name, priority, AFB=None, spaceCannon=None, faction=None):
        self.cost=cost
        self.hit=hit
        self.hp=hp
        self.capacity=capacity
        self.name=name
        self.priority=priority
        self.AFB = AFB
        self.spaceCannon = spaceCannon
        self.faction=faction
        
    def __str__(self):
        """Print the name and hp of the ship."""
        return(f"Ship Name: {self.name}, HP: {self.hp}")
    def __repr__(self):
        return(f"Ship Name: {self.name}, HP: {self.hp}")
        
    ##Flagship Combat Phase Special abilities, overwritten only by specific flagships
        
    def BeforeModifier(self,enemyFleet):
        pass
    
    def RollModifier():
        pass
    
    def StartofCombatLoop():
        pass
        
    def HitModifier():
        pass

# Example usage

class Fighter(Ship):
    def __init__(self, upgrade=False, faction=None):
        if upgrade:
            super().__init__(0.5, 8, -1, 1,"Fighter",1)
        else:
            super().__init__(0.5, 9, -1, 1,"Fighter",1)
        
    
class Carrier(Ship):
    def __init__(self, upgrade=False, faction=None):
        if upgrade:
            super().__init__(3, 9, 6, 1,"Carrier",2)
        else:
            super().__init__(3, 9, 4, 1,"Carrier",2)
            
class Cruiser(Ship):
    def __init__(self, upgrade=False, faction=None):
        if upgrade:
            super().__init__(2, 3, 1, 1,"Cruiser",3)
        else:
            super().__init__(2, 7, 0, 1,"Cruiser",3)
                
        
class Destroyer(Ship):
    def __init__(self, upgrade=False, faction=None):
        if upgrade:
            super().__init__(1, 8, 0, 1,"Destroyer",4,AFB=[6,6,6])
        else:
            super().__init__(1, 9, 0, 1,"Destroyer",4,AFB=[9,9])
                
class Dreadnaught(Ship):
    def __init__(self, upgrade=False, faction=None):
        if upgrade:
            super().__init__(4, 5, 1, 2,"Dreadnaught",5)
        else:
            super().__init__(4, 5, 1, 2,"Dreadnaught",5)
                
           
        
class Warsun(Ship):
    def __init__(self,  faction=None):
        super().__init__(12, [3,3,3], 6, 2,"Warsun",7) #flagship is 6
                
                
               
class Flagship(Ship):
    def __init__(self, faction):
        flagships = {
            "Arborec": [8, [7, 7], 5, 2, "Arborec Flagship", 6],
            "Barony": [8, [5, 5], 3, 2, "Barony Flagship", 6],
            "Saar": [8, [5, 5], 3, 2, "Saar Flagship", 6, [6,6,6,6]],
            "Muaat": [8, [5, 5], 3, 2, "Muaat Flagship", 6],
            "Hacan": [8, [7, 7], 3, 2, "Hacan Flagship", 6],  # pay 1 trade good, +1 to die roll, 1/roll. All rolls in system. (ROLLS)
            "Sol": [8, [5, 5], 12, 2, "Sol Flagship", 6],
            "Ghost": [8, [5], 3, 2, "Ghost Flagship", 6],
            "L1Z1X": [8, [5, 5], 5, 2, "L1Z1X Flagship", 6],  # hits produced by this ship and dreadnoughts are assigned to non-fighters if able (HITS)
            "Mentak": [8, [7, 7], 3, 2, "Mentak Flagship", 6],  # Other player's ship cannot use sustain damage (BEFORE)
            "Naalu": [8, [9, 9], 6, 2, "Naalu Flagship", 6],
            "Nekro": [8, [9, 9], 3, 2, "Nekro Flagship", 6],  # Ground forces participate in space combat (??)
            "Sardakk": [8, [6, 6], 3, 2, "Sardakk Flagship", 6],  # +1 to each ship combat in system (ROLLS)
            "Jol-Nar": [8, [6, 6], 3, 2, "Jol-Nar Flagship", 6],  # When this ship rolls 9/10, (before mods), produce 2 additional hits (HITS)
            "Winnu": [8, 7, 3, 2, "Winnu Flagship", 6],  # Roll dice equal to the # of opponent's non-fighter ships (StartofCombatLoop)
            "Xxcha": [8, [7, 7], 3, 2, "Xxcha Flagship", 6, [5,5,5]], ##SPACE CANNON RACE
            "Yin": [8, [9, 9], 3, 2, "Yin Flagship", 99],  # When Destroyed, destroy all ships (Assign Hits/END)
            "Yssaril": [8, [5, 5], 3, 2, "Yssaril Flagship", 6],
            "Argent": [8, [7, 7], 3, 2, "Argent Flagship", 6],  # no space cannon against you (Before)
            "Empyrean": [8, [5, 5], 3, 2, "Empyrean Flagship", 6],  # 2 influence to repair sustain in system (START of COMBAT LOOP)
            "Mahact": [8, [3, 3], 3, 2, "Mahact Flagship", 6],  # Combat against opponent whose command token is not in your fleet pool, +2 to this unit's combat rolls, was [5,5], changed to [3,3]
            "NaazRokha": [8, [9, 9], 4, 2, "Naaz Flagship", 6],
            "Nomad": [8, [7, 7], 3, 2, "Nomad Flagship", 6, [8,8,8]],  ### UPGRADE [8,[5,5],6,2,"Nomad Flagship", 6,[5,5,5]] (POTENTIAL UPGRADE)
            "Ul": [8, [7, 7], 3, 2, "Ul Flagship", 6],
            "Cabal": [8, [5, 5], 3, 2, "Cabal Flagship", 6],
            "Keleres": [8, [7, 7], 6, 2, "Keleres Flagship", 6]
        }
        
        match faction:
            case "Mentak":
                self.BeforeModifier = self.MentakBeforeModifier
            case "Empyrean":
                self.StartofCombatLoop = self.EmpyreanStartofCombatLoop
            case "Hacan":
                self.RollModifier = self.HacanRollModifier
            case "Sardakk":
                self.RollModifier = self.SardakkRollModifier
            case "Jol-Nar":
                self.HitModifier = self.JolNarHitModifier
            case "Winnu":
                self.StartofCombatLoop = self.WinnuStartofCombatLoop
            case "Yin":
                self.BeforeModifier = self.YinBeforeModifier
            case "Argent":
                self.BeforeModifier = self.ArgentBeforeModifier
            case "L1Z1X":
                self.HitModifier = self.L1Z1XHitModifier

            
        
        f = flagships[faction]
        
        if faction=="Xxcha":
            super().__init__(f[0], f[1], f[2], f[3], f[4], f[5], spaceCannon=f[6],faction=faction)
        elif len(f) == 6:  # Base
            super().__init__(f[0], f[1], f[2], f[3], f[4], f[5],faction=faction)
        elif len(f) == 7:  # AFB
            super().__init__(f[0], f[1], f[2], f[3], f[4], f[5], AFB=f[6],faction=faction)
        
    ##BEFORE MODIFIER 
    def MentakBeforeModifier(self,enemyFleet):
        for ship in enemyFleet:
            ship.hp=1
            
    def YinBeforeModifier(self,enemyFleet): ##returns true flag that will be checked to let Yin always win
        return True
            
    ##Start of Combat Loop (Empyrean)
    def EmpyreanStartofCombatLoop(self): #Repair self
        self.hp=2
            
    def WinnuStartofCombatLoop(self,enemyFleet):
        self.hit=[]
        for ship in enemyFleet:
            if not isinstance(ship,Fighter):
                self.hit.append(7)
            
    def ArgentBeforeModifier(self,enemyFleet):
        for ship in enemyFleet:
            ship.spaceCannon = None
            
            
    ##ROLL Modifier
    def HacanRollModifier(self,rolls):
       rolls = rolls + 1
    
    def SardakkRollModifier(self,rolls):
        rolls = rolls + 1
            
    ##Assign Hit Modifier
    def JolNarHitModifier(self,rolls, hits):
        for roll in rolls[:2]:
            if roll>=9:
                hits=hits+1
    
    def L1Z1XHitModifier(self,rolls,hits,alliedFleet,enemyFleet): #check which rolls correspond to dreadnoughts and self' assign them to non-fighter units
        directHitters = [] #indices of rolls/hits that will be calculated and assigned directly to enemy fleet
        index=0 #current index
        
        ##get indices
        for ship in alliedFleet:    
            if isinstance(ship,(Dreadnaught, Flagship)): 
                hitLen=0 #may get type error
                try:
                    hitLen=len(ship.hit)
                except TypeError as e:
                    hitLen=1
                print("HitLen: ",hitLen)
                
                while hitLen>0:
                    directHitters.append(index)
                    index=index+1
                    hitLen=hitLen-1
            
        
        rolls2 = rolls[directHitters]
        hits2 = hits[directHitters]
        
        h = np.sum(hits2 <= rolls2)
        
        #if wipeout
        if h>=len(enemyFleet):
            enemyFleet=[] #wiped out
        
        
        ##Assign Hits
        # Iterate through the fleet and remove the first N non-Fighter ships
        enemyFleetCopy=enemyFleet
        while h>0:
            for ship in enemyFleetCopy:  # Iterate over a copy of the list
                if not isinstance(ship, Fighter):
                    fleet.remove(ship)  # Remove the non-Fighter ship
                    h = h - 1
        #hit some fighters next
        if h>0:
            enemyFleetCopy=enemyFleetCopy[h:]
            
        print("NEEDS TESTING!!!")
            
        enemyFleet=enemyFleetCopy