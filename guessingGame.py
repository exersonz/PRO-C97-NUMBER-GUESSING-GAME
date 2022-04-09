import random

randomNumber = random.randrange(1, 9)
chances = 0

print("Number guessing game!")
print("Guess a number between 1 and 9.")
print("You have 5 chances, good luck!")

while chances < 5:
    guess = int(input("Enter your guess: "))
    chances += 1

    if guess < randomNumber:
        print("Your guess was too low! Guess a number higher than ", guess)

    elif guess > randomNumber:
        print("Your guess was too high! Guess a number lower than ", guess)

    else:
        print("Congratulations, you win!!")
        break

    if not chances < 5:
        print("Sorry, you lost! The number is ", randomNumber)