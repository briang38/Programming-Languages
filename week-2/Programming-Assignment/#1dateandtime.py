"""
(30pts) Write a Python program to display the current date and time. (Must be the time that you run this program at. Otherwise, you won’t get points.)
In the following output: 

# Current date and time :

# YYYY-mm-dd H:M:S

Sample Output :

Current date and time :
2021-12-28 18:05:43
"""

#Brian Gutt


from datetime import datetime

# this grabs the current date and time locally
now = datetime.now()

# This displays the output in 24-hour format
# This progam calls for the 24 hour time 
print("Current date and time :")
print(now.strftime("%Y-%m-%d %H:%M:%S\n"))