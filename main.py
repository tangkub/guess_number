# Guess the nubmer

# import random module
import random

# function: guess the number
def GuessNum(num):
    num_rand = random.randint(1, num)
    num_guess = 0
    print(f"Let's guess the number between 1 and {num}")

    while num_guess != num_rand:
        num_guess = int(input("Your number: "))
        if num_guess > num_rand:
            print(f"{num_guess} is too high.")
        elif num_guess < num_rand:
            print(f"{num_guess} is too low.")

    print(f"Congrant! The correct number is {num_rand}")

# run function by num=10
GuessNum(10)