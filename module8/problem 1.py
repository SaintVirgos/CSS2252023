#Zaineb Bonilla
#11/21/2023
#Problem 1 – Write a function that takes two inputs from a user and prints
# whether they are equal or not.

def is_equal(num1, num2):
    if int(num1) == int(num2):
        print("Numbers are equal")
    else:
        print("Numbers are not equal")
is_equal(5,10)
is_equal(5,5)

# Number1 = int(input('please enter your first number'))
#
# Number2 = int(input('please enter your second number'))
#
# if Number1 > Number2:
#     print('Number1 bigger than Number2')
# elif Number1 < Number2:
#     print('Number1 smaller than Number2')
# else:
#     print('Number1 equal to Number2')