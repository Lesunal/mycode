#!/usr/bin/env python3
"""Number guessing game! User has 5 chances to guess a number between 1 and 100!"""
import random

def main():
    num= random.randint(1,100)

    rounds= 0
    guess= 0

    while rounds < 5 and guess != num:
        guess= input("Guess a number between 1 and 100\n>")

        # COOL CODE ALERT: what is the purpose of the next four lines?
        if guess.isdigit():
            guess= int(guess)
            rounds+=1
        else:
            continue

        if guess > num:
            print("Too high!")
        elif guess < num:
            print("Too low!")
        else:
            print("Correct!")

main()