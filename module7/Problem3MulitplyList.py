#Zaineb Bonilla
#11/20/2023
#Problem 3: Write a Python function to multiply all the numbers in a list.
# Use list [5, 2, 7,-1]

def multiplylist(list):
    total = 1 #set total to 1, so we can add onto it
    for i in list: #i changes to the next item, every loop
        total = total * i
        print(total)





list = [5,2,7,-1]
multiplylist(list) #takes the list, puts it into multiplylist