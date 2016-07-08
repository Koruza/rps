from random import randint
import time

#Goal
#Ask the player if they pick rock paper or scissors
#Have the computer chose its move
#Compare the choices and decide who wins
#Print the results
#Subgoals
#Let the player play again
#Keep a record of the score e.g. (Player: 3 / Computer: 6)


possibleMoves = ['rock','paper', 'scissors']

def aihand():
    hand = randint(0,2)
    print("AI hand %s" %(hand))
    return hand

def game(ai, player):
    if ai == player:
        winner = "Tie"
    elif (ai == 0 and player == 1) or (ai == 1 and player == 2) or (ai == 2 and player == 0):
    	winner = "You"
    else:
        winner = "Computer"
	return winner

def play():
    CompW = 0
    YourW = 0
    Ties = 0
    print("Rock, Paper, Scissors, Shoot!")

    yourHand = raw_input("Which hand do you choose? ")
    yourHand = possibleMoves.index(yourHand.lower())
    print("Your hand %s" %(yourHand))

    ai = aihand()
    if ai == yourHand:
        winner = "Tie"
    elif (ai == 0 and yourHand == 1) or (ai == 1 and yourHand == 2) or (ai == 2 and yourHand == 0):
        winner = "You"
    else:
        winner = "Computer"
  
    print("The computer played %s and you played %s" %(possibleMoves[ai], possibleMoves[yourHand]))
    if winner == "Tie":
        Ties +=1
        print("It is a tie")
    elif winner == "You":
        YourW +=1
        print("You won!")
    else:
        CompW +=1
        print("The Computer Wins")
    return


play()