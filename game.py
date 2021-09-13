import random

name = input("Howdy, what's your name? ") 
print(name + ", I'm thinking of a number between 1 and 100.\nTry to guess my number.")

number = random.randint(1, 100)
count = 0

while True:
    count += 1
    guess = int(input("Your guess? "))
    if (guess > number):
        print("Your guess is too high, try again.")
    elif (guess < number):
        print("Your guess is too low, try again.")
    else:
        print("Well done, " + name + "! You found my number in " + str(count) + " tries!")
        break