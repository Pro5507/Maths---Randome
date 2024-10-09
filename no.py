import random
play= True
no= random.randint(10 ,20)
print("I will generate a number from 10 to 20 and you have to guess the number")
while play:
    guess= input("Give me your best guess: \n")
    if no==guess:
        print("You win the game",no)
        break
    else:
        print("Try aganin \n")