import random

def heading():

    print("Guessing Game!\n\n")

heading()

def Game():
    NumLimit = input("Enter a limit: ")

    while not NumLimit.isdigit():
        NumLimit = input("Please type in a digit: ")

    NumLimit = int(NumLimit)

    print("Ok, guess a number between 0 and", NumLimit)

    RandomNum = (random.randint(0,NumLimit))

    NumGuess = int(input())

    while NumGuess != RandomNum:

        if NumGuess < RandomNum:
            print("A little bit higher!")
            NumGuess = int(input())

        elif NumGuess > RandomNum:
            print("A little bit lower!")
            NumGuess = int(input())

            
    print("You guessed it!")

Game()

Again = input("Do you want to play again? Type in y or n\n")

while Again.lower() != "y" or "n":
    Again = input("Type only in y or n\n")
    print()

if Again.lower() == "y":
   Game()
    
elif Again.lower() == "n":
      print("Bye bye!")




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





