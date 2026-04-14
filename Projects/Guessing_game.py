# Guessing Game

import random
target = random.randint(1,100)
guess = int(input("Guess any number: "))

count =0

while target!=guess:

    if(guess>target):
        print("Guess lower")
        count += 1
    else:
        print("Guess higher")
        count += 1
    guess = int(input("Guess again: "))
   
print("Correct guess")
print("Total attempts: ", count)
