#Treydon Olfert
#December 6th, 2022
#Guessing Game
#Computer Science 20
#-----------------------------------------------------------
#Libraries
from random import randint
import os
from time import sleep
#-----------------------------------------------------------
#Variables
initialguesscount1 = 0
initialguesscount2 = 0
hintfrequency = ""
warning = ""
hints = ""
shufflefrequency = ""
shuffle = ""
highrange = ""
lowrange = ""
guess = ""
difficulty = "" #Blank strings just so that they're defined and .lower() can be used
#-----------------------------------------------------------
#Shuffle check function. This checks if the number should be shuffled by checking the difference of guesscount from initialguesscount (which only changes when it's set to guesscount after a shuffle) and then comparing it to the shufflefrequency.
def shufflecheck():
  global guesscount, initialguesscount1, shufflefrequency, lowrange, highrange, guess, num
  if guesscount - initialguesscount1 >= int(shufflefrequency) and int(guess) != num:
    initialguesscount1 = guesscount
    num = randint(int(lowrange), int(highrange))
    guess = input("Wrong. Number shuffled. Try again: ")
    guesscount += 1
    while not guess.isdigit(): #This while loop is used after every time the user is prompted with any input throughout the program. It checks for invalid responses and excludes "quit" and "main menu", in which it breaks until reaching the end of the code with "quit" or goes to line [] to go back to the main menu if the input was "main menu"
      if guess.lower() == "quit" or guess.lower() == "main menu":
        break
      else:
        guess = input("Invalid. Try again: ")
    if guess.lower() != "quit" and guess.lower() != "main menu":
      shufflecheck()
#-----------------------------------------------------------
#Hint check function. It checks if a hint should be given using the same method as shufflecheck(). A hint is given by randomly choosing one from the hintlist list variable and then deleting that hint to prevent it from being chosen again.
def hintcheck():
  global guesscount, initialguesscount2, hintfrequency, guess, num, hintnum
  if guesscount - initialguesscount2 >= int(hintfrequency) and int(guess) != num:
    initialguesscount2 = guesscount
    if len(hintlist) == 0:
      print("No more hints to give!")
    else:
      hintnum = randint(0, len(hintlist) - 1)
      print("Here's a hint: " + hintlist[hintnum])
      del hintlist[hintnum]
#-----------------------------------------------------------
#Main Guessing Game Function. Starts by resetting certain variables so that previous games don't interfere with the new one and then checks if the difficulty was custom, in which it prompts the user for the custom difficulty's settings while also constantly checking for invalid responses or "quit" or "main menu". These invalid checks often use str(x).lower() because it allows the inputs to not be case sensitive and doing .lower() on a non-string value causes an error. A warning is also given if hints are enabled and the highrange is greater than or equal 1,000,000 because it can take a long time to calculate the hints or just stops working completely.
def guessinggame():
  global guess, guesscount, initialguesscount1, initialguesscount2, lowrange, highrange, shuffle, shufflefrequency, lowermessage, highermessage, firsttrymessage, num, hintlist, hintfrequency, hintnum, hints, warning
  hintlist = []
  guesscount = 0
  initialguesscount1 = 0
  initialguesscount2 = 0
  warning = "Y"
  hints = "disabled"
  composite = False
  while difficulty.lower() == "c": #This is where the user creates their custom difficulty
    lowrange = input("What's the lowest number that can be picked? ")
    while not lowrange.isdigit():
      if lowrange.lower() == "quit" or lowrange.lower() == "main menu":
        break
      else:
        lowrange = input("Invalid. Try again: ")
    if lowrange.lower() == "quit" or lowrange.lower() == "main menu":
      break
    highrange = input("What's the highest number that can be picked? ")
    while not highrange.isdigit():
      if highrange.lower() == "quit" or highrange.lower() == "main menu":
        break
      else:
        highrange = input("Invalid. Try again: ")
    if highrange.lower() == "quit" or highrange.lower() == "main menu":
      break
    shuffle = input("Will number shuffling be on (Y/N)? ")
    while shuffle.lower() != "y" and shuffle.lower() != "n":
      if shuffle.lower() == "quit" or shuffle.lower() == "main menu":
        break
      else:
        shuffle = input("Invalid. Try again: ")
    if shuffle.lower() == "quit" or shuffle.lower() == "main menu":
      break
    elif shuffle.lower() == "y":
      shuffle = "enabled"
      shufflefrequency = input("How often should the number be shuffled (in # of guesses)? ")
      while not shufflefrequency.isdigit():
        if shufflefrequency.lower() == "quit" or shufflefrequency.lower() == "main menu":
          break
        else:
          shufflefrequency = input("Invalid. Try again: ")
      if shufflefrequency.lower() == "quit" or shufflefrequency.lower() == "main menu":
        break
    elif shuffle.lower() == "n":
      shuffle = "disabled"
    if shuffle == "disabled":
      hints = input("Will hints be on (Y/N)? ")
    while hints.lower() != "y" and hints.lower() != "n" and hints.lower() != "disabled" and hints.lower() != "enabled":
      if hints.lower() == "quit" or hints.lower() == "main menu":
        break
      else:
        hints = input("Invalid. Try again: ")
    if hints.lower() == "quit" or hints.lower() == "main menu":
      break
    while str(hints).lower() == "y" and str(warning).lower() == "y":
      if int(highrange) >= 1000000:
        warning = input("WARNING: Having hints enabled at such a high number could cause the program to not work or it will take a significant amount of time to calculate the hints. Keep hints enabled? (Y/N) ")
        while warning.lower() != "y" or warning.lower() != "n":
          if warning.lower() == "quit" or warning.lower() == "main menu":
            break
          else:
            warning = input("Invalid. Try again: ")
        if warning.lower() == "quit" or warning.lower() == "main menu":
          break
        if warning == "N":
          hints = "disabled"
          break
      hintfrequency = input("How often should a hint be given (in # of guesses)? ")
      while not hintfrequency.isdigit():
        if hintfrequency.lower() == "quit" or hintfrequency.lower() == "main menu":
          break
        else:
          hintfrequency = input("Invalid. Try again: ")
      hints = "enabled"
    if hints == "N":
      hints = "disabled"
    highermessage = "The number is higher. Try again: "
    lowermessage = "The number is lower. Try again: "
    firsttrymessage = "Congratulations. You got it first try."
    break
#-----------------------------------------------------------
#The Guessing Game. First generates the random number, then checks if hints are enabled and generates them if so. Then the game actually starts. With each input, the game checks if the input is invalid, "main menu", or "quit", then checks if a shuffle or hint needs to happen using shufflecheck() and hintcheck(). It does this until the input equals the number. It then congratulates you and tells you how many guesses it took. It then uses sleep() from the time library to pause the program for 5 seconds and then it goes back to the main menu and the cycle continues.
  if str(hintfrequency).lower() != "quit" and str(hintfrequency).lower() != "main menu" and str(warning).lower() != "quit" and str(warning).lower() != "main menu" and str(hints).lower() != "main menu" and str(hints).lower() != "quit" and str(shufflefrequency).lower() != "quit" and str(shufflefrequency).lower() != "main menu" and str(shuffle).lower() != "quit" and str(shuffle).lower() != "main menu" and str(highrange).lower() != "quit" and str(highrange).lower() != "main menu" and str(lowrange).lower() != "quit" and str(lowrange).lower() != "main menu":
    num = randint(int(lowrange),int(highrange))
    #-----------------------------------------------------------
    #Hint generating. If hints are enabled, it first checks if the number is prime or composite, checks if the number is even or odd, checks how many digits the number is, and checks what numbers are multiples of the random number and then adds them all to a list variable called hintlist.
    if hints == "enabled":
      if num > 1:
        for number in range(2, num):
          if num % number == 0:
            composite = True
            break
        if composite: #add digit counter
          hintlist.append("The number is composite.")
        else:
          hintlist.append("The number is prime.")
      if num % 2 == 0:
        hintlist.append("The number is even.")
      else:
        hintlist.append("The number is odd.")
      hintlist.append("The number is " + str(len(str(num))) + " digits.")
      for number in range (3, num):
        if num % number == 0:
          hintlist.append("The number is a multiple of " + str(number))
    #-----------------------------------------------------------
    if difficulty.lower() == "gj":
      guess = input("Guess the number. (Game Journalist hint: the number is " + str(num) + "): ") #The game journalist hint is different from the custom mode's hint system.
    else:
      guess = input("Guess the number: ")
    guesscount += 1
    while not guess == str(num):
      while not guess.isdigit():
        if guess.lower() == "quit" or guess.lower() == "main menu":
          break
        else:
          guess = input("Invalid. Try again: ")
      if guess.lower() == "quit" or guess.lower() == "main menu":
        break
      if shuffle == "enabled":
        shufflecheck()
      if hints == "enabled":
        hintcheck()
      if guess.lower() == "quit" or guess.lower() == "main menu":
        break
      if int(guess) > num:
        guess = input(lowermessage)
        guesscount += 1
      while not guess.isdigit():
        if guess.lower() == "quit" or guess.lower() == "main menu":
          break
        else:
          guess = input("Invalid. Try again: ")
      if guess.lower() == "quit" or guess.lower() == "main menu":
        break
      if shuffle == "enabled":
        shufflecheck()
      if hints == "enabled":
        hintcheck()
      if guess.lower() == "quit" or guess.lower() == "main menu":
        break
      if int(guess) < num:
        guess = input(highermessage)
        guesscount += 1
  if str(guess).lower() != "quit" and str(guess).lower() != "main menu" and str(hintfrequency).lower() != "quit" and str(hintfrequency).lower() != "main menu" and str(warning).lower() != "quit" and str(warning).lower() != "main menu" and str(hints).lower() != "main menu" and str(hints).lower() != "quit" and str(shufflefrequency).lower() != "quit" and str(shufflefrequency).lower() != "main menu" and str(shuffle).lower() != "quit" and str(shuffle).lower() != "main menu" and str(highrange).lower() != "quit" and str(highrange).lower() != "main menu" and str(lowrange).lower() != "quit" and str(lowrange).lower() != "main menu":
    if guesscount > 1:
      print("Congratulations. You got it in " + str(guesscount) + " tries.")
      if difficulty.lower() == "gj":
        print("Loser.") #It says what the number is and they took more than 1 try. 
      sleep(5)
      mainmenu()
    else:
      print(firsttrymessage) 
      sleep(5)
      mainmenu()
  elif str(guess).lower() == "main menu" or str(hintfrequency).lower() == "main menu" or str(warning).lower() == "main menu" or str(hints).lower() == "main menu" or str(shufflefrequency).lower() == "main menu" or str(shuffle).lower() == "main menu" or str(highrange).lower() == "main menu" or str(lowrange) == "main menu":
    mainmenu()
#-----------------------------------------------------------
#Main Menu Function. Uses os.system('clear') to clear the console, then shows the difficulty selection.
def mainmenu():
  os.system('clear')
  global difficulty
  difficulty = input("Guess the Number Game! \nChoose a difficulty: \nGame Journalist (GJ) - The number will be either 1 or 2 and you get a hint.\nEasy (E) - The number will be chosen from 1 to 5.\nMedium (M) - The number will be chosen from 1 to 10\nHard (H) - The number will be chosen from 1 to 100 \nNightmare (N) - The number will be chosen from 1 to 1000 \nUltra Nightmare (UN) - The number will be chosen from 1 to 100,000 and you won't be told whether your guess was higher or lower.\nImpossible (I) - The number will be chosen from 1 to 292,201,338 and the number is shuffled with each guess.\nCustom (C)\nYou can type \"quit\" to leave the game or \"main menu\" to come back to this menu at any time.\n")
#-----------------------------------------------------------
mainmenu() #This is the first thing to run in the program
#-----------------------------------------------------------
#Difficulty check and setup. Checks what difficulty was typed in the main menu and sets the variables accordingly and then goes to the guessinggame() function except the custom difficulty, which has its variables set from inputs in the guessinggame() function
while difficulty.lower() != "quit" and str(guess).lower() != "quit" and str(hintfrequency).lower() != "quit" and str(warning).lower() != "quit" and str(hints).lower() != "quit" and str(shufflefrequency).lower() != "quit" and str(shuffle).lower() != "quit" and str(highrange).lower() != "quit" and str(lowrange).lower() != "quit": #This is the main loop of the game and the only way out is if quit is typed at any input.
  if difficulty.lower() == "gj":
    lowrange = 1
    highrange = 2
    shuffle = "disabled"
    lowermessage = "The number is lower. Try again: "
    highermessage = "The number is higher. Try again: "
    firsttrymessage = "Congratulations. You got it first try."
    guessinggame()
    
  elif difficulty.lower() == "e":
    lowrange = 1
    highrange = 5
    shuffle = "disabled"
    lowermessage = "The number is lower. Try again: "
    highermessage = "The number is higher. Try again: "
    firsttrymessage = "Congratulations. You got it first try. There was a 20% chance of that happening."
    guessinggame()
    

  elif difficulty.lower() == "m":
    lowrange = 1
    highrange = 10
    shuffle = "disabled"
    lowermessage = "The number is lower. Try again: "
    highermessage = "The number is higher. Try again: "
    firsttrymessage = "Congratulations. You got it first try. There was a 10% chance of that happening."
    guessinggame()

  elif difficulty.lower() == "h":
    lowrange = 1
    highrange = 100
    shuffle = "disabled"
    lowermessage = "The number is lower. Try again: "
    highermessage = "The number is higher. Try again: "
    firsttrymessage = "Congratulations. You got it first try. There was a 1% chance of that happening."
    guessinggame()

  elif difficulty.lower() == "n":
    lowrange = 1
    highrange = 1000
    shuffle = "disabled"
    lowermessage = "The number is lower. Try again: "
    highermessage = "The number is higher. Try again: "
    firsttrymessage = "Congratulations. You got it first try. There was a 0.1% chance of that happening."
    guessinggame()
  
  elif difficulty.lower() == "un":
    lowrange = 1
    highrange = 100000
    shuffle = "disabled"
    lowermessage, highermessage = "Wrong. Try again: ", "Wrong. Try again: "
    firsttrymessage = "Congratulations. You got it first try. There was a 0.001% chance of that happening."
    guessinggame()

  elif difficulty.lower() == "i":
    lowrange = 1
    highrange = 292201338
    shuffle = "enabled"
    shufflefrequency = 1
    lowermessage, highermessage = "You shouldn't be seeing this. Please report this bug to the game developer. :) ", "You shouldn't be seeing this. Please report this bug to the game developer. :) " #It's supposed to shuffle every guess so they shouldn't see either of the higher or lower messages.
    firsttrymessage = "Cheater. The odds of doing this were the same as buying 1 ticket to the Powerball lottery and winning the jackpot. Get lost."
    guessinggame()

  elif difficulty.lower() == "c":
    guessinggame()

  elif difficulty.lower() == "main menu":
    mainmenu()

  else:
    while difficulty.lower() != "c" and difficulty.lower() != "i" and difficulty.lower() != "un" and difficulty.lower() != "n" and difficulty.lower() != "h" and difficulty.lower() != "m" and difficulty.lower() != "e" and difficulty.lower() != "gj" and difficulty.lower() != "quit" and difficulty.lower() != "main menu":
      difficulty = input("Invalid. Try again: ")
#-----------------------------------------------------------