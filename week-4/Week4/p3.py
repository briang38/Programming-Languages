"""
Brian Gutt

Problem #3

(30pts) Check if an expression is balanced by its parentheses or not. 
Sample expression: ((a+b)

Sample Output: False

Sample expression: (((a+b)+c)+d)+e 

Sample Output: True

"""

def is_balanced(expression):
    stack = []
    for char in expression:
        if char == '(':
            # Push opening parenthesis to the stack
            stack.append(char)
        elif char == ')':
            # If stack is empty or no matching opening parenthesis
            if not stack or stack[-1] != '(':
                return False
            # Pop the matching opening parenthesis
            stack.pop()
    # If stack is empty, the expression is balanced
    return not stack

# Sample Input 1
expression1 = "((a+b)"
print(is_balanced(expression1))  # Output: False

# Sample Input 2
expression2 = "(((a+b)+c)+d)+e"
print(is_balanced(expression2))  # Output: True