##Simulate equal Pts with different makeups
from Ships.Ships import *
import numpy as np
from itertools import combinations
import csv
from datetime import datetime
import sys

MaxRounds=500


# Define the Ship Vectors
vectors = np.array([
    [0.5, -1],  # Fighter
    [3, 4],    # Carrier
    [2, 0],     # Cruiser
    [1, 0],     # Destroyer
    [4, 1],     # Dreadnaught
    [12, 6]     # Warsun
])


def sort_key(ship):
    # If hit is a list, use the first element; otherwise, use the hit value directly
    hit_value = ship.hit[0] if isinstance(ship.hit, list) else ship.hit
    return (-hit_value, ship.priority)  # Sort by hit value

def find_all_combinations(N, capacity):
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
                                 
                            C = a2 + a3 + a4 +a5  + a6 
                            
                            # Check the conditions
                            if X == N and Y >= 0 and C <=capacity:
                                solutions.append((int(a1), int(a2), int(a3), int(a4), int(a5), int(a6), 0))
    
    return solutions

def createFleet(fleet):
    #print("Creating Fleet: ",fleet)
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
    
def assignHits(fleet1,hits, AFB=0): #TODO use fleet2 for better hit assignment
    #assign hits to members of fleet1,
    #CHALLENGE: varying ordering of destroyer
    #print("Assign:\t\tHits: ",hits, ", Fleet: ",fleet1)
    
    if hits==0:
        return fleet1
    
    if AFB==1:
        for f in fleet1:
            if f.name=="Fighter":
                fleet1.remove(f)
                hits=hits-1
                if hits<1: #no more AFB
                    return fleet1
    else:
        #Use sustain
        for f in fleet1:
            if f.hp>1:
                f.hp=f.hp-1
                hits=hits-1
                #print("SUSTAIN HIT: ",hits)
                if hits<1:
                    #print("NO casualties")
                    return fleet1
               
        #kill worse ships according to sort
        if hits<len(fleet1):
            fleet1 = sorted(fleet1, key=sort_key)  # Sort fleet1 using the sort_key function
            fleet1=fleet1[hits:]
            
        else:
            #print("Fleet wiped out")
            fleet1.clear()
            
    return fleet1
    



def Combat(fleet1,fleet2):
    #create fleets
    f1=createFleet(fleet1)
    f2=createFleet(fleet2)
    
    f10=f1
    f20=f2
    

    #Combat
    f1stat=[0,0,0]
    f2stat=[0,0,0]
    
 


    
    #Repeat for 100 Rounds
    for i in range(MaxRounds):
        f1=f10
        f2=f20
        round=1
        
        ##Anti-Fighter Barrage, happens only at start
        f1AFB = [f.AFB for f in f1]
        f2AFB = [f.AFB for f in f2]
        
        NoNone1AFB = [item for item in f1AFB if item is not None] #remove none
        NoNone2AFB = [item for item in f2AFB if item is not None] #remove none
        
        flat1AFB = np.array(NoNone1AFB).flatten() #flatten
        flat2AFB= np.array(NoNone2AFB).flatten() #flatten
        
        #roll dice
        r1 = np.random.randint(0, 10, size=len(flat1AFB))
        r2 = np.random.randint(0, 10, size=len(flat2AFB))
        
        #compare two
        h1 = np.sum(flat1AFB <= r1)
        h2 = np.sum(flat2AFB <= r2)
        
        #assign hits
        if h2>0:
            #print("\n\nFleet 1: ")
            #print("\n\nAssign Hits: ")
            #print(f1)
            f1=assignHits(f1,h2,1)
            #print(f1)
        
        if h1>0:     
            #print("\n\nFLEET 2:")
            #print(f2)
            f2=assignHits(f2,h1,1)
            #print(f2)
        
        
        
        while (len(f1)>0 and len(f2) > 0): #while someone has units
            #print("\n\n COMBAT ROUND: ",round)
            #print(len(f1))
            #print(len(f2))
            round=round+1
            
            ##Regular Combat
            #Get hit
            #print(f1)
            
            f1hit = [item.hit for sublist in f1 for item in (sublist if isinstance(sublist, list) else [sublist])]
            f2hit = [item.hit for sublist in f2 for item in (sublist if isinstance(sublist, list) else [sublist])]
                        
            #print(f1hit)
            #print(f2hit)
            
            for f in f1hit:
                #print(f," - ",isinstance(f,list))
                if isinstance(f,list):
                    for ff in f:
                        f1hit.append(ff)
                    f1hit.remove(f)

            #print("F2hit: ", f2hit)
            for f in f2hit:
                #print(f)
                if isinstance(f,list):
                    for ff in f:
                        f2hit.append(ff)
                    f2hit.remove(f)       

            #print(f1hit)
            #print(f2hit)
            
            #roll dice
            r1 = np.random.randint(0, 10, size=len(f1hit))
            r2 = np.random.randint(0, 10, size=len(f2hit))
            
            #print(r1)
            
            #compare two
            h1 = np.sum(f1hit <= r1)
            h2 = np.sum(f2hit <= r2)
            
            #print(h1)
            #print(h2)
            
            #assign hits
            if h2>0:
                #print("\n\nFleet 1: ")
                #print("\n\nAssign Hits: ")
                #print(f1)
                f1=assignHits(f1,h2)
                #print(f1)
            
            if h1>0:     
                #print("\n\nFLEET 2:")
                #print(f2)
                f2=assignHits(f2,h1)
                #print(f2)
                
                
        ##SCORING      
        if len(f1)==len(f2)==0: #Draw
            f1stat[2]= f1stat[2]+1
            f2stat[2]= f2stat[2]+1
        elif len(f1)==0: #F2 Wins
            f1stat[1]= f1stat[1]+1
            f2stat[0]= f2stat[0]+1
        elif len(f2)==0: #F1 Wins
            f1stat[0]= f1stat[0]+1
            f2stat[1]= f2stat[1]+1    
        
            
    f1score = f1stat[0] + (f1stat[2]/2)
    f2score = f2stat[0] + (f2stat[2]/2)
    #print("W/L/D: ",f1stat)
    return [f1score,f2score]
    




def Simulate(cost, capacity):
    N =  cost# Example value for N
    print("Create all Fleet Combinations: ",N)
    fleets = find_all_combinations(N, capacity)
    #for fleet in fleets:
        #print(f"Fleet: {fleet}")

    print("\n\nBegin Combat")

    #match all combinations:
    matchups = list(combinations(range(0,len(fleets)), 2))
    #for m in matchups:
        #print(m)
        

    #combat
    mNumber=0
    for matchup in matchups:
        mNumber=mNumber+1
        print(mNumber/len(matchups))
        #print("Matchup: ",fleets[matchup[0]],fleets[matchup[1]])
        [f1score,f2score] =Combat(fleets[matchup[0]],fleets[matchup[1]])
        #print(f1score)
        #print(f2score)
        #print( fleets[matchup[0]][-1])
        
        fleets[matchup[0]] = fleets[matchup[0]][:-1] + (fleets[matchup[0]][-1] + f1score,)
        fleets[matchup[1]] = fleets[matchup[1]][:-1] + (fleets[matchup[1]][-1] + f2score,)
     
     
     
     
    print("\nSave Results")
    
    numRounds=((len(fleets)-1)*MaxRounds)
     
    #print("NumRounds: ",numRounds)
     
     
   
    for f in fleets:
        #print(f)
        fleetSize=np.sum(f[:-1]) - f[0]
        #print("fleetSize: ",fleetSize)
        f=np.append(f,[fleetSize,f[-1]/numRounds, N])
        results.append(f)
        
    # Get the current timestamp and format it
    #timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  # Format: YYYYMMDD_HHMMSS
    filename = f'Results\TIResults_Cost_{N}_Capacity_{capacity}.csv'  # Create the filename with timestamp
        
    # Open the CSV file with newline='' to prevent extra new lines
    with open(filename, 'w', newline='') as f:
        # Using csv.writer method from CSV package
        write = csv.writer(f)
        fields = ["Fighters","Carriers","Cruisers","Destroyers","Dreadnaught","Warsun","Score", "FleetSize","WinRate", "Cost"]
        write.writerow(fields)  # Write the header
        write.writerows(results)  # Write the data rows



##GLOBAL VARIABLES
results=[]


#MAIN
if __name__ == "__main__":
    
    total_args = len(sys.argv) - 1  # Subtract 1 to exclude the script name
    
    for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"Argument {i}: {arg}")
    
    fleetCapacity=6
    
    for cost in range(2,21): #cost is cost
        Simulate(cost,fleetCapacity)
        results=[]