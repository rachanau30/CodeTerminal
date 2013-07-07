#-----------------------------------------------------------
#This code is created by https://codeterminal.wordpress.com/
#-----------------------------------------------------------
#The Classic Rock-Paper-Scissors game in Python.
#The winner of Rock Paper Scissors is determined as follows:
#Rock defeats Scissors.
#Scissors defeats Paper.
#Paper defeats Rock.
#------------------
#Human vs Computer

#import the random module so that the computer can choose
#either Rock or Paper or Scissors at random
import random

#import some system specific parameters and functions using 
#the sys module
import sys


def makeYourChoice():

    print "Press R for Rock"
    print "Press P for Paper"
    print "Press S for Scissors"
    print "Press Q to quit!"

    userChoice = raw_input("What do you want to choose? \n").lower()

    if userChoice == "r":
        return "Rock"

    if userChoice == "p":
        return "Paper"

    if userChoice == "s":
        return "Scissors"

    if userChoice == "q":
        sys.exit(0)

    else:
        makeYourChoice()


def computerRandom():

    options = ["Rock","Paper","Scissors"]
    randomChoice = random.randint(0,2)
    return options[randomChoice]



def comparison(humanChoice, computerChoice):

    if humanChoice == computerChoice:
        return "Draw"

    if humanChoice == "Rock" and computerChoice == "Paper":
        return "Computer Wins"

    if humanChoice == "Paper" and computerChoice == "Scissors":
        return "Computer Wins"

    if humanChoice == "Scissors" and computerChoice == "Rock":
        return "Computer Wins"

    else: return "Human Wins"




humanChoice = makeYourChoice()
computerChoice =  computerRandom()


print "You chose: ", humanChoice
print "The computer chose: ", computerChoice

result = comparison (humanChoice, computerChoice)


if result == "Draw":
  print "Its a draw"

elif result == "Computer Wins":
	print "Unlucky you lost!"

else: 
	print "Well done you won!"


