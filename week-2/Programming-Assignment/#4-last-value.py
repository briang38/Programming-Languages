"""
(30pts) Write a Python program with a function to replace last value of tuples in a list. 
Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

Sample Output:

[(10, 20, 1000), (40, 50, 1000), (70, 80, 1000)]

"""

#Brian Gutt

def replace_last_value(tuples_list, new_value):
    # Create a new list with the last value of each tuple replaced
    updated_list = [t[:-1] + (new_value,) for t in tuples_list]
    return updated_list

# Sample list of tuples
sample_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

# New value to replace the last element of each tuple
new_value = 1000

# Call the function and print the result
updated_list = replace_last_value(sample_list, new_value)
print(updated_list)