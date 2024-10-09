import random
a= random.randint(10,20)
b= int(input("Enter a guess"))
if a==b:
    print("you won")
else:
    print("Please try again \n")