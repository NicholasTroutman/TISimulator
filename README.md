# TISimulator
Combat Simulator for Twilight Imperium 4th Edition

## GOAL
Create combat metrics for cost efficiency of each unit via monte-carlo simulation.

## Questions:
1. Baseline composition setups w/ same Cost
	1a. 3-5
	1b. 6-10
	1c. 11-15
	1d. 16-20
2. Most cost efficient ships?
3. Which Compositions punch above their weight class
4. Best upgrades?


## Conclusions:
1. Higher fleet capacity are more efficient. Massing Destroyers is really good, but capacity inefficient.
2. Fighters are bad until 12/13 cost, 5/6 capacity respectively


## Problems:
Destroyers are over-emphasized since fighters make up so much of the low-ranks.
Split field in half and rerun calculations.

Add Flagships

flagships = {
"Arborec": [8,[7,7], 5, 2,"Arborec Flagship", 6],
"Barony": [8,[5,5],3, 2, "Barony Flagship", 6],
"Saar":  [8,[5,5], 3,2,"Saar Flagship", 6, [6,6,6,6]],
"Muaat": [8,[5,5], 3,2,"Muaat Flagship", 6],
"Hacan": [8,[7,7], 3,2, "Hacan Flagship", 6], #pay 1 trade good, +1 to die roll, 1/roll. All rolls in system.
"Sol":  [8,[5,5],12,2,"Sol Flagship", 6],
"Ghost":  [8,[5],3,2,"Ghost Flagship", 6],
"L1Z1X": [8,[5,5],5,2,"L1Z1X Flagship", 6], #hits produced by this ship and dreadnaughts are assigned to non-fighters if able
"Mentak": [8,[7,7],3,2,"Mentak Flagship", 6], #Other player's ship cannot use sustain damage
"Naalu": [8, [9,9],6,2,"Naalu Flagship", 6], 
"Nekro": [8,[9,9],3,2,"Nekro Flagship", 6], #Ground forces participate in space combat
"Sardakk": [8,[6,6],3,2,"Sardaak Flagship", 6], #+1 to each ship combat in system
"Jol-Nar": [8,[6,6],3,2,"Jol-Nar Flagship", 6], #When this ship rolls 9/10, (before mods), produce 2 additional hits
"Winnu": [8,7,3,2,"Winnu Flagship", 6], #Roll dice equal to the # of opponent's non-fighter ships
"Xxcha": [8,[7,7],3,2,"Xxcha Flagship", 6], #Space Cannon 5(x3), adjacent attacks
"Yin": [8,[9,9],3,2,"Yin Flagship", 6], #When Destroyed, destroy all ships
"Yssaril": [8,[5,5],3,2,"Yssaril Flagship", 6],
"Argent": [7,[7,7],3,2,"Argent Flagship", 6], #no space cannon against you
"Empyrean": [8,[5,5],3,2,"Emyprean Flagship", 6], #2 influence to repair sustain in system
"Mahact": [8,[5,5],3,2,"Mahact Flagship", 6], #Combat against opponent whose command token no in ur fleet pool, +2 to this unit's combat rolls
"NaazRokha": [8, [9,9], 4,2,"Naaz Flagship", 6],
"Nomad": [8,[7,7],3,2,"Nomad Flagship",6,[8,8,8], #UPGRADE [8,[5,5],6,2,"Nomad Flagship", 6,[5,5,5]]
"Ul":[8,[7,7],3,2,"Ul Flagship", 6],
"Cabal": [8, [5,5], 3,2,"Cabal Flagship",6],
"Keleres": [8,[7,7],6,2,"Keleres Flagship", 6]
}