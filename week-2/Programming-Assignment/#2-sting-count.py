"""
(30pts) Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. 
Sample List : 

['abcdefg', 'kkzz', 'aba', '3528', ‘6006’, ‘3214’, ‘zrkz’]

Sample Output :

3
"""

#Brian Gutt

def count_matching_strings(words):
    count = 0
    for word in words:
        if len(word) >= 2 and word[0] == word[-1]:
            count += 1
    return count

# Sample List
sample_list = ['abcdefg', 'kkzz', 'aba', '3528', '6006', '3214', 'zrkz']

# Output result
result = count_matching_strings(sample_list)
print(result)


