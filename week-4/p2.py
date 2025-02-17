"""
Brian Gutt

Problem 2

(30pts) Write a Python program to find out all index locations that has a certain pattern a string. (return a list, return [] if no such pattern in the string.)
Sample String : “abaaababbbbaaabbabababababbbaaaaabababababbbbb”

            Pattern: “abb”

Sample Output :

[6, 13, 24, 40]

"""

def find_pattern_indices(input_string, pattern):
    pattern_length = len(pattern)
    indices = []
    for i in range(len(input_string) - pattern_length + 1):
        # Check if the substring matches the pattern
        if input_string[i:i+pattern_length] == pattern:
            indices.append(i)
    return indices

# Sample Input
input_string = "abaaababbbbaaabbabababababbbaaaaabababababbbbb"
pattern = "abb"

# Find the indices
output = find_pattern_indices(input_string, pattern)

# Print the output
print(output)