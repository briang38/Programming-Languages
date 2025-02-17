"""
Brian Gutt

Problem #1

(30pts) Write a Python program to display a string’s index 0, 1, 2, 6, 7, 8, 12, 13, 14, 18, 19, 20, … (3 on and 3 off pattern) location characters for any string given.  
Sample Input String: “abcdefghijklmnopqrstuvwxyz”

Sample Output :

abcghimnostuyz


"""

def display_pattern_characters(input_string):
    result = ""
    i = 0
    while i < len(input_string):
        # Add the next 3 characters
        result += input_string[i:i+3]
        # Skip the next 3 characters
        i += 6
    return result

# Sample Input
input_string = "abcdefghijklmnopqrstuvwxyz"

# Get the result
output = display_pattern_characters(input_string)

# Print the output
print(output)