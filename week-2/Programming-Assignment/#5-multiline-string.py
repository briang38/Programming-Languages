"""
(30pts) Write a Python program to split a given multiline string into a list of lines. 
Original string: 

This

is a

multiline

string.

Split the said multiline string into a list of lines

Sample Output:

['This', 'is a', 'multiline', 'string.', '']

"""

#Brian Gutt

# Original multiline string
multiline_string = """This

is a

multiline

string."""

# Split the multiline string into a list of lines
lines_list = multiline_string.splitlines()
# Remove empty strings from the list
lines_list = [line for line in multiline_string.splitlines() if line]

# Print the result
print(lines_list)
