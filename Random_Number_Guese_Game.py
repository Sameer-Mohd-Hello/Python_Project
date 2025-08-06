import random as rd

a = rd.randint(1,10)

while True:
    b = int(input("Guess a number between 1 and 10-> "))
    if b == a:
        print("You guessed it! The number was ->", a)
        break
    elif b > a :
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")
