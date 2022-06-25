import random

choices = ["rock", "paper", "scissor"]

compGuess = random.choice(choices)

player = None
tie = False

print("---Welcome to Rock-Paper-Scisor---")
print("---Enjoy!!!---")

ready = input("Are you fready?(y/n):\n").lower()
if ready == 'y':
    myGuess = input("Your choice: rock(r), paper(p), scissor(s):\n").lower()
else:
    quit()

if myGuess == 'r':
    player = "rock"
elif myGuess == 'p':
    player = "paper"
elif myGuess == 's':
    player = "scissor"

if player == compGuess:
    tie = True
    myGuess = input("Your choice: rock(r), paper(p), scissor(s):\n").lower()

def game(player, compGuess):
    if tie:
        print("You Guessed:", player)
        print("computer guessed:", compGuess)
        print("It's a Tie!!!!")
    elif player == "rock":
        print("You Guessed:", player)
        print("computer guessed:", compGuess)
        if compGuess == "scissor":
            print("You win!!!!")
        elif compGuess == "paper":
            print("You lost!!!!")
    elif player == "paper":
        print("You Guessed:", player)
        print("computer guessed:", compGuess)
        if compGuess == "rock":
            print("You win!!!!")
        elif compGuess == "scissor":
            print("You lost!!!!")
    elif player == "scissor":
        print("You Guessed:", player)
        print("computer guessed:", compGuess)
        if compGuess == "paper":
            print("You win!!!!")
        elif compGuess == "rock":
            print("You lost!!!!")

if player not in choices:
    myGuess = input("Your choice: rock(r), paper(p), scissor(s):\n").lower()
else:
    game(player, compGuess)