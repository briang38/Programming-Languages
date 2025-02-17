"""
Brian Gutt

Problem #5

(30pts) Given a list of number from 1 to N. The list has only one missing number. (within 1 to N). Please find out which number is missing. (Sorting not allowed. O(n) algorithm required)
Sample Input Sequence: [3, 5, 2, 1]   # missing 4

Sample Output: 4 
"""

def find_missing_number(nums):
    n = len(nums) + 1  # Alg for one missing num
    expected_sum = n * (n + 1) // 2  # sum of numbers from 1 to N
    actual_sum = sum(nums)  # Actual sum of the given list
    return expected_sum - actual_sum  # Missing number

# Sample Input
nums = [3, 5, 2, 1]
print(find_missing_number(nums))  # Output: 4