##Simulate equal Pts with different makeups
from Ships.Ships import *
import numpy as np
from scipy.optimize import linprog

# Define the coefficients of the vectors
coefficients = np.array([
    [0.5, -1],  # Fighter
    [3, 4],     # Carrier
    [2, 0],     # Cruiser
    [1, 0],     # Destroyer
    [4, 1],     # Dreadnaught
    [12, 6]     # Warsun
])

# Define the target value for X
N = 12

# Objective function: We want to minimize the sum of coefficients (not really important here)
c = np.zeros(6)  # Coefficients for a_1, a_2, ..., a_6

# Equality constraint: 0.5a_1 + 3a_2 + 2a_3 + 1a_4 + 4a_5 + 12a_6 = N
A_eq = np.array([coefficients[:, 0]])  # Coefficients for X
b_eq = np.array([N])  # Right-hand side for equality

# Inequality constraint: -1a_1 + 4a_2 + 0a_3 + 0a_4 + 1a_5 + 6a_6 >= 0
A_ineq = np.array([-coefficients[:, 1]])  # Coefficients for Y
b_ineq = np.array([0])  # Right-hand side for inequality

# Bounds for each coefficient (a_i >= 0)
bounds = [(0, None) for _ in range(6)]

# Solve the linear programming problem
result = linprog(c, A_eq=A_eq, b_eq=b_eq, A_ub=A_ineq, b_ub=b_ineq, bounds=bounds, method='highs')

# Check if the optimization was successful
if result.success:
    print("Optimal coefficients found:")
    print(result.x)  # This will give the coefficients a_1, a_2, ..., a_6
else:
    print("No solution found.")
    




print("SIMULATING")

