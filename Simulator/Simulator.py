##Simulate equal Pts with different makeups
from Ships.Ships import *
import numpy as np
from itertools import combinations

# Define the Ship Vectors
vectors = np.array([
    [0.5, -1],  # Fighter
    [3, 4],     # Carrier
    [2, 0],     # Cruiser
    [1, 0],     # Destroyer
    [4, 1],     # Dreadnaught
    [12, 6]     # Warsun
])

def find_all_combinations(N):
    solutions = []
    
    # Limit for coefficients (you can adjust this based on your needs)
    max_coeff = (N //vectors[:, 0] +1) # Convert to integer

    max_coeff = max_coeff.astype(int)
    
    #print(max_coeff)
   
    # Iterate through possible coefficients
    #print("START RANGE")
    for a1 in range(0,max_coeff[0],2):
        #print("\n\nFighter: ",a1)
        for a2 in range(0,max_coeff[1],1):
            #print("Carrier: ",a2)
            for a3 in range(0,max_coeff[2],1):
                #print("Cruiser:",a3)
                for a4 in range(0,max_coeff[3],1):
                    #print("Destroyer:",a4)
                    for a5 in range(0,max_coeff[4],1):
                        #print("Dreadnaught:",a5)
                        for a6 in range(0,max_coeff[5],1):
                            #print("Warsun:",a6)
                            ## Calculate the resulting vector
                            X = (a1 * vectors[0][0] + a2 * vectors[1][0] +
                                 a3 * vectors[2][0] + a4 * vectors[3][0] +
                                 a5 * vectors[4][0] + a6 * vectors[5][0])
                            
                            Y = (a1 * vectors[0][1] + a2 * vectors[1][1] +
                                 a3 * vectors[2][1] + a4 * vectors[3][1] +
                                 a5 * vectors[4][1] + a6 * vectors[5][1])
                            
                            # Check the conditions
                            if X == N and Y >= 0:
                                solutions.append((int(a1), int(a2), int(a3), int(a4), int(a5), int(a6), int(X), int(Y)))
    
    return solutions

def createFleet(fleet):
    newFleet=[]
    
    for i in range(fleet[0]):
        newFleet.append(Fighter())
        
    for i in range(fleet[1]):
        newFleet.append(Carrier())
       
    for i in range(fleet[2]):
        newFleet.append(Cruiser())
        
    for i in range(fleet[3]):
        newFleet.append(Destroyer())
        
    for i in range(fleet[4]):
        newFleet.append(Dreadnaught())
        
    for i in range(fleet[5]):
        newFleet.append(Warsun())
    
    return(newFleet)
    
def assignHits(fleet1,fleet2,hits):
    #assign hits to members of fleet1,
    #CHALLENGE: varying ordering of destroyer

def Combat(fleet1,fleet2):
    #create fleets
    f1=createFleet(fleet1)
    f2=createFleet(fleet2)
    

    #Combat
    f1stat=[0,0,0]
    f2stat=[0,0,0]
    
    print(f1)
    
    while (len(f1)>0 or len(f2) > 1): #while someone has units
        #Get hit
        f1hit = np.array([f.hit for f in f1])
        f2hit = np.array([f.hit for f in f2])
        
        print(f1hit)
        print(f2hit)
        
        #roll dice
        r1 = np.random.randint(0, 10, size=len(f1hit))
        r2 = np.random.randint(0, 10, size=len(f2hit))
        
        #compare two
        h1 = np.sum(f1hit >= r1)
        h2 = np.sum(f2hit >= r2)
        
        print(h1)
        print(h2)
        
        #assign hits
        
        exit()
    
    

if __name__ == "__main__":
    
    print("Create all Fleet Combinations: ")
    N = 5  # Example value for N
    fleets = find_all_combinations(N)
    for fleet in fleets:
        print(f"Fleet Combination: {fleet[:-2]}, Resulting Vector: ({fleet[-2]}, {fleet[-1]})")

    print("\n\nBegin Combat")

    #match all combinations:
    matchups = list(combinations(range(0,len(fleets)), 2))

    #combat
    for matchup in matchups:
        Combat(fleets[matchup[0]],fleets[matchup[1]])
        exit()



