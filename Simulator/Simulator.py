##Simulate equal Pts with different makeups
from Ships.Ships import *
import numpy as np
from itertools import combinations
import csv
from datetime import datetime
import sys
import os


MaxRounds=400


# Define the Ship Vectors, as basic
vectors = np.array([
    [0.5, -1],  # Fighter
    [3, 4],    # Carrier
    [2, 0],     # Cruiser
    [1, 0],     # Destroyer
    [4, 1],     # Dreadnaught
    [8, 3],      #Flagship *TENTATIVE 1
    [12, 6]     # Warsun
])

factions = ["Arborec",
            "Barony",
            "Saar",
            "Muaat",
            "Hacan",
            "Sol",
            "Ghost",
            "L1Z1X",
            "Mentak",
            "Naalu",
            "Nekro",
            "Sardakk",
            "Jol-Nar",
            "Winnu",
            "Xxcha",
            "Yin",
            "Yssaril",
            "Argent",
            "Empyrean",
            "Mahact",
            "NaazRokha",
            "Nomad",
            "Ul",
            "Cabal",
            "Keleres"]

def read_first_half_of_rows(directory):
    """Reads the first half of all rows from each CSV file in the specified directory."""
    results = {}  # Dictionary to store results for each file

    # Iterate through each file in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.csv'):  # Check for CSV files
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as f:
                reader = csv.reader(f)
                header = next(reader)  # Read the header
                rows = list(reader)  # Read all rows into a list

                # Calculate the number of rows to read (first half)
                
                half_index = len(rows) // 2
                first_half_rows = rows[:half_index]  # Get the first half of the rows

                # Store the results in the dictionary
                results[filename] = {
                    'header': header,
                    'first_half': first_half_rows
                }
                #print("\n\n")
                #print(filename,"  --  ",len(results[filename]), "  - ",len(rows)," ~ ",half_index)
                #print(results[filename])
                #print("\n")
                #print(results[filename]['first_half'])
                #print(results[filename])

    return results #in a dictionary, results[filename]['first_half'] to get data in list of lists



def sort_key(ship):
    # If hit is a list, use the first element; otherwise, use the hit value directly
    hit_value = ship.hit[0] if isinstance(ship.hit, list) else ship.hit
    return (-hit_value, ship.priority)  # Sort by hit value





def find_all_combinations(N, capacity):
    solutions = []
    
    for faction in factions:
        #print(faction)
        
        ##Define Flagship vector
        vectors[6][1]=Flagship(faction).capacity
        
        ##TODO upgrades for other ships
        
        # Limit for coefficients (you can adjust this based on your needs)
        max_coeff = (N //vectors[:, 0] +1) 

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
                            #print("Flagship:",a5)
                                for a7 in range(0,max_coeff[6],1):
                                    #print("Warsun:",a6)
                                    
                                    ## Calculate the resulting vector
                                    X = (a1 * vectors[0][0] + a2 * vectors[1][0] +
                                         a3 * vectors[2][0] + a4 * vectors[3][0] +
                                         a5 * vectors[4][0] + a6 * vectors[5][0] + a7*vectors[6][1])
                                    
                                    Y = (a1 * vectors[0][1] + a2 * vectors[1][1] +
                                         a3 * vectors[2][1] + a4 * vectors[3][1] +
                                         a5 * vectors[4][1] + a6 * vectors[5][1] + a7*vectors[6][1])
                                         
                                    C = a2 + a3 + a4 +a5  + a6 
                                    
                                    # Check the conditions
                                    if X == N and Y >= 0 and C <=capacity:
                                        solutions.append((int(a1), int(a2), int(a3), int(a4), int(a5), int(a6), int(a7), faction, 0))
            
   # print(solutions)
    #exit()
    return solutions

def createFleet(fleet):
    #print("Creating Fleet: ",fleet)
    fleetFaction=fleet[7]
    
    newFleet=[]
    
    for i in range(fleet[0]):
        newFleet.append(Fighter(faction=fleetFaction))
        
    for i in range(fleet[1]):
        newFleet.append(Carrier(faction=fleetFaction))
       
    for i in range(fleet[2]):
        newFleet.append(Cruiser(faction=fleetFaction))
        
    for i in range(fleet[3]):
        newFleet.append(Destroyer(faction=fleetFaction))
        
    for i in range(fleet[4]):
        newFleet.append(Dreadnaught(faction=fleetFaction))
        
    for i in range(fleet[5]):
        newFleet.append(Flagship(faction=fleetFaction))
        
    for i in range(fleet[6]):
        newFleet.append(Warsun(faction=fleetFaction))
    
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
    
    f10=f1.copy()
    f20=f2.copy()
    

    #Combat
    f1stat=[0,0,0]
    f2stat=[0,0,0]
    
 

    #print("Fleet1:\t",fleet1)
    #print("Fleet2:\t",fleet2)    
    
    #Repeat for 100 Rounds
    for i in range(MaxRounds):
        #print(i,":\t",f1stat, " - ",f2stat)
        f1=f10.copy()
        f2=f20.copy()
        #print(f1," - ",f2)
        
        ##Before Flagship Modifier
        flag1 = next((flagship for flagship in f1 if isinstance(flagship, Flagship)), Ship(0,0,0,0,"SHIP",0)) #return default ship instead 
        flag2 = next((flagship for flagship in f2 if isinstance(flagship, Flagship)), Ship(0,0,0,0,"SHIP",0)) #return default ship instead
        
        Yin1= flag1.BeforeModifier(f2)
        Yin2= flag2.BeforeModifier(f1)
   
   
        ##Space Cannon
        f1SC = [f.spaceCannon for f in f1]
        f2SC = [f.spaceCannon for f in f2]
        
        NoNone1SC = [item for item in f1SC for item in f1SC if item is not None]
        NoNone2SC = [item for item in f2SC for item in f2SC if item is not None]
        
        flat1SC = np.array(NoNone1SC).flatten() #flatten
        flat2SC= np.array(NoNone2SC).flatten() #flatten
        
        #roll dice
        r1 = np.random.randint(0, 10, size=len(flat1SC))
        r2 = np.random.randint(0, 10, size=len(flat2SC))
        
        #compare two
        h1 = np.sum(flat1SC <= r1)
        h2 = np.sum(flat2SC <= r2)
        
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
        
        
        
        ##Anti-Fighter Barrage, happens only at start
        f1AFB = [f.AFB for f in f1]
        f2AFB = [f.AFB for f in f2]
        
        #print(f2AFB)
        NoNone1AFB=[]
        NoNone2AFB=[]
        for afb in f1AFB:
            if isinstance(afb,list):
                for a in afb:
                   NoNone1AFB.append(a)
        for afb in f2AFB:
            if isinstance(afb,list):
                for a in afb:
                   NoNone2AFB.append(a)          
                
        #print(NoNone2AFB)
        
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
            f1=assignHits(f1,h2,AFB=1)
            #print(f1)
        
        if h1>0:     
            #print("\n\nFLEET 2:")
            #print(f2)
            f2=assignHits(f2,h1,AFB=1)
            #print(f2)
        
        
        
        ##Regular Combat
        round=1
        #print("\n\n")
        while (len(f1)>0 and len(f2) > 0): #while someone has units
            #print("\n\n COMBAT ROUND: ",round)
            #print(len(f1))
            #print(len(f2))
            round=round+1
            
            ##Regular Combat
            #Get hit
            f1hit = [item.hit for sublist in f1 for item in (sublist if isinstance(sublist, list) else [sublist])]
            f2hit = [item.hit for sublist in f2 for item in (sublist if isinstance(sublist, list) else [sublist])]
                                   
            
            ##flatten list
            for f in f1hit.copy():
                #print(f," - ",isinstance(f,list))
                if isinstance(f,list):
                    for ff in f:
                        f1hit.append(ff)
                    f1hit.remove(f)

            #print("F2hit: ", f2hit)
            for f in f2hit.copy():
                #print(f)
                if isinstance(f,list):
                    for ff in f:
                        f2hit.append(ff)
                    f2hit.remove(f)       

            #print("tohit 1: ",f1hit)
            #print("tohit 2: ",f2hit)
            
            #roll 
            r1 = np.random.randint(0, 10, size=len(f1hit))
            r2 = np.random.randint(0, 10, size=len(f2hit))
            
            #print("\nr1: ",r1)
            #print("r2: ",r2)
            #compare two
            
            h1 = np.sum(f1hit <= r1)
            h2 = np.sum(f2hit <= r2)
            
            #print(h1)
            #print(h2)
            
            #assign hits
            if h1>0:     
                #print("hits 1: ",h1)
                f2=assignHits(f2,h1)
            
            if h2>0:
                #print("hits 2: ",h2)
                f1=assignHits(f1,h2)
                            

                
                
        ##SCORING      
        
        if len(f1)==0 and not Yin1: #F2 Wins, unless F1 has Yin Flagship
            f1stat[1]= f1stat[1]+1
            f2stat[0]= f2stat[0]+1
        elif len(f2)==0 and not Yin2: #F1 Wins, unless F2 has Yin Flagship
            f1stat[0]= f1stat[0]+1
            f2stat[1]= f2stat[1]+1 
        else: #Draw
            f1stat[2]= f1stat[2]+1
            f2stat[2]= f2stat[2]+1
        
            
    f1score = f1stat[0] + (f1stat[2]/2)
    f2score = f2stat[0] + (f2stat[2]/2)
    #print("W/L/D: ",f1stat)
    return [f1score,f2score]
    




def Simulate(cost, capacity, subdir, faction): #Currently 1 faction only
    #print("\nSimulate: ",cost, " - ", capacity, " - ",faction)
    N =  cost# Example value for N
    #print("Create all Fleet Combinations: ",N)
    fleets = find_all_combinations(N, capacity)
    #print("!!!! NUM FLEETS: ",len(fleets))
    for fleet in fleets.copy():
        #print(f"Fleet: {fleet}")
        if fleet[5]==0 and fleet[7]!='Arborec':
            fleets.remove(fleet)
            #print(f"Fleet REMOVE: {fleet}")

    #print("\n\nBegin Combat")

    #match all combinations:
    matchups = list(combinations(range(0,len(fleets)), 2))
        

    #combat
    #mNumber=0
    for matchup in matchups:
        #mNumber=mNumber+1
        #print(mNumber/len(matchups))
        #print("Matchup: ",fleets[matchup[0]],fleets[matchup[1]])
        [f1score,f2score] =Combat(fleets[matchup[0]],fleets[matchup[1]]) #TODO: MAke different factions
        #print(f1score)
        #print(f2score)
        #print( fleets[matchup[0]][-1])
        
        fleets[matchup[0]] = fleets[matchup[0]][:-1] + (fleets[matchup[0]][-1] + f1score,)
        fleets[matchup[1]] = fleets[matchup[1]][:-1] + (fleets[matchup[1]][-1] + f2score,)
     
     
     
     
    #print("\nSave Results")
    
    numRounds=((len(fleets)-1)*MaxRounds)
     
    #print("NumRounds: ",numRounds)
    results=[]
    for f in fleets:
        
        #print("\n\nORDER\n")
        #print([row[6] for row in results])
        #resultsSorted = sorted(results, key=lambda x: x[7], reverse=True)
        #print([row[6] for row in resultsSorted])

        #print(f)
        fleetSize=np.sum(f[1:6])
        #print("fleetSize: ",fleetSize)
        #print("Score: ",f[-1], "\tnumrounds: ",numRounds,"WinRate: ",f[-1]/numRounds)
        f=np.append(f,[fleetSize,f[-1]/numRounds, N])
        results.append(f)
    
    resultsSorted = sorted(results, key=lambda x: x[10], reverse=True)
   

    # Get the current timestamp and format it
    #timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  # Format: YYYYMMDD_HHMMSS
    filename = f"{subdir}\TIResults_Cost_{N}_Capacity_{capacity}.csv"  # Create the filename with variables
        
    #print("!!!! NUM resultsSorted: ",len(resultsSorted))
    # Open the CSV file with newline='' to prevent extra new lines
    with open(filename, 'w', newline='') as f:
        # Using csv.writer method from CSV package
        write = csv.writer(f)
        fields = ["Fighters","Carriers","Cruisers","Destroyers","Dreadnaught","Flagship","Warsun","Faction","Score", "FleetSize","WinRate", "Cost"]
        write.writerow(fields)  # Write the header
        write.writerows(resultsSorted)  # Write the data rows






##GLOBAL VARIABLES
results=[]

def createAllSimulations(cost,fleetCapacity,subdir):
    for fleetCapacity in range(fleetCapacity[0],fleetCapacity[1]):
        for cost in range(12,cost):
            print(f"Cost: {cost} - Fleet Capacity: {fleetCapacity}\n")
            Simulate(cost,fleetCapacity,subdir, factions[0]) #Arborec
            results=[]
        
        
#MAIN
if __name__ == "__main__":
    
    total_args = len(sys.argv) - 1  # Subtract 1 to exclude the script name
    
    for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"Argument {i}: {arg}")
       


    createAllSimulations(14,[3,5],"Results\\testStuff")
    exit()

        
    
    directory = "Results/BasicResults"
    halfData = read_first_half_of_rows(directory)
    
    ##Scrape the data into fleets:
    for filename in os.listdir(directory):
        print(filename, "\n",halfData[filename]['first_half'])
        print("\n\n")
            

    
    
    exit()
    
    
    
    createAllSimulations(4,5,"Results/testStuff")
    exit()