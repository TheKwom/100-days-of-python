# Day 4 - Rock, Paper, Scissors
import random

userChoice = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors.\n"))
compChoice = random.randint(0,2)

resultsMessage = ""
game_strings = ["rock", "paper", "scissors"]

if 0 <= userChoice <= 2:
    print("You chose " + game_strings[userChoice] + ".")
    print("Computer chose " + game_strings[compChoice] + ".")

if userChoice < 0 or userChoice > 2:
    print("Invalid input. You lose")
elif userChoice == 0 and compChoice == 2:
    resultsMessage = "You win!"
elif compChoice == 0 and userChoice == 2:
    resultsMessage = "You lose."
elif userChoice < compChoice:
    resultsMessage = "You lose."
elif userChoice > compChoice:
    resultsMessage = "You win!"
elif userChoice == compChoice:
    resultsMessage = "Draw."

print(resultsMessage)
