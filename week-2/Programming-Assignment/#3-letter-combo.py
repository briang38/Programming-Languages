"""
(30pts) Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary. 
Sample data : {'1':['x', 'y', 'z'], '2':['s', 't']}

Sample Output:

xs

xt

ys

yt

zs

zt

"""

#Brian Gutt

import itertools

# Sample data
data = {'1': ['x', 'y', 'z'], '2': ['s', 't']}

# Extract the lists from the dictionary
lists = list(data.values())

# Compute the Cartesian product of the lists
combinations = itertools.product(*lists)

# Display all combinations
for combination in combinations:
    print(''.join(combination))