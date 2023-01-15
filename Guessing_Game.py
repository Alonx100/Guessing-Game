#GuessingGame Made by Alon Rehin for CIS 261

import random

def heading():

    print("Guessing Game!\n\n")

heading()

def Game():

    count = 1

    NumLimit = input("Enter a limit: ")

    while not NumLimit.isdigit():
        NumLimit = input("Please type in a digit: ")

    NumLimit = int(NumLimit)

    print("\nOk, guess a number between 0 and", NumLimit)

    RandomNum = (random.randint(0,NumLimit))

    NumGuess = int(input())

    while NumGuess != RandomNum:

        if NumGuess < RandomNum:
            count += 1
            print("\nA little bit higher!\n")  
            NumGuess = int(input())

        elif NumGuess > RandomNum:
            count += 1
            print("\nA little bit lower!\n")
            NumGuess = int(input())

            
    print("You guessed it in", count,"tries\n")

    Again = input("Do you want to play again? Type in y or n\n")

    while Again.lower() != "y" and Again.lower() != "n":
        Again = input("Type only in y or n\n")
        print()

    if Again.lower() == "y":
       Game()
    
    elif Again.lower() == "n":
          print("Bye bye!\n")

Game()






#while not NumGuess.isdigit():
 #   print("Please type in a digit: ")
  #  NumGuess = input("Your guess is: ")
   # 
    #if NumGuess.isdigit():
     # NumGuess = int(NumGuess)
     #
  #  if NumGuess == RandomNum:
   #    print("Wrong number try again!")
    #   Numguess = input("Your next guess is: ")
    #
   # else:
    #    print("Congratulation, you have won!")





