"""
Brian Gutt

Problem #4

(30pts) Write a program to print out tower(n), 
Sample Output:

tower(1)

/\

**

**

tower(2)

 /\

 **

 **

/ \

* *

* *

tower(3)

 /\

 **

 **

 / \

 * *

 * *

/   \

*   *

*   *
"""

def tower(n):
    # Calculate the width of the base
    base_width = 2 * n - 1

    # Print the top part of the tower
    print(" " * (n - 1) + "/\\" + " " * (n - 1))
    print(" " * (n - 1) + "**" + " " * (n - 1))
    print(" " * (n - 1) + "**" + " " * (n - 1))

    # Print the middle and base parts of the tower
    for i in range(1, n):
        # Print the top of the current level
        print(" " * (n - i - 1) + "/" + " " * (2 * i) + "\\" + " " * (n - i - 1))
        # Print the base of the current level
        print(" " * (n - i - 1) + "*" + " " * (2 * i) + "*" + " " * (n - i - 1))
        print(" " * (n - i - 1) + "*" + " " * (2 * i) + "*" + " " * (n - i - 1))

# Test cases
print("tower(1)")
tower(1)
print("\ntower(2)")
tower(2)
print("\ntower(3)")
tower(3)