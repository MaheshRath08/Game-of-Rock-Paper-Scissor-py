import random

choices = ["rock", "paper", "scissor"]  

compGuess = random.choice(choices)  #computer's guess

player = None     #declaring the variables early 
tie = False

print("---Welcome to Rock-Paper-Scisor---")  #welcome
print("---Enjoy!!!---")                      #message

ready = input("Are you fready?(y/n):\n").lower()    #asking the user if he's ready or not
if ready == 'y':                            
    myGuess = input("Your choice: rock(r), paper(p), scissor(s):\n").lower()       
else:
    quit()
#converting user input to something comparable to the computer's guesses
if myGuess == 'r':
    player = "rock"
elif myGuess == 'p':
    player = "paper"
elif myGuess == 's':
    player = "scissor"
#if ties, it keeps on asking for input
if player == compGuess:
    tie = True
    myGuess = input("Your choice: rock(r), paper(p), scissor(s):\n").lower()

def game(player, compGuess):            #declairing the game function with arguments such as player and compguess
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

if player not in choices:               #a condition to take proper user input
    myGuess = input("Your choice: rock(r), paper(p), scissor(s):\n").lower()
    print("type either 'r', 'p' or 's'")
else:
    game(player, compGuess)