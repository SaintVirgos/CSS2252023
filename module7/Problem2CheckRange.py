#Zaineb Bonilla
#11/20/2023
#Problem 2: Write a Python function to check whether a number is in a given range.
# Use range(1,10). Print whether the number is in or not in the range.

def checkRange(number):
    if number in range(1,10):
        print("yes in range")
    else:
        print("not in range")
(checkRange(9))