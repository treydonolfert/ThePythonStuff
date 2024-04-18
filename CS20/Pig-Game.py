#Pig Game Project
#Treydon Olfert
#Computer Science 20
#January 26, 2023
#--------------------------------------------------------
from random import randint
#----------------------------Milestone #1----------------------------
def milestone1(num=0,score1=0,turntotal=0,turn=1): #I used default arguments because I think it's easier to read since I can look to these for reference rather than going down to when the function was called and trying to figure out which argument is which.
  while score1 < 100:
    print("Turn #" + str(turn))
    while num != 1 and turntotal < 20 and turntotal + score1 < 100:
      num = randint(1,6)
      if num == 1:
        turntotal = 0
      else:
        turntotal += num
      print("Die roll: " + str(num) + "\nTurn total so far: " + str(turntotal))
    print("Turn total: " + str(turntotal))
    score1 += turntotal
    turntotal = 0
    num = 0
    print("Score: " + str(score1))
    turn += 1
#----------------------------Milestone #2----------------------------
def milestone2(num=0,score1=0,score2=0,turntotal=0,turn=1):
  while score1 < 100 and score2 < 100:
    print("Player " + str(turn) + "'s turn")
    while num != 1 and turntotal < 20 and turntotal + (score1 if turn==1 else score2) < 100: #If it's the first player's turn it checks if the turntotal + first player's score < 100 and if it's the second player's turn it checks if the turntotal + second player's score < 100 instead
      num = randint(1,6)
      if num == 1:
        turntotal = 0
      else:
        turntotal += num
      print("Die roll: " + str(num) + "\nTurn total so far: " + str(turntotal))
    print("Turn total: " + str(turntotal))
    if turn == 1:
      score1 += turntotal
      print("Score: " + str(score1))
    else:
      score2 += turntotal
      print("Score: " + str(score2))
    turntotal = 0
    num = 0
    turn = 3 - turn #3 - turn will always just alternate the turn between 1 and 2 since turn starts at 1.
  if score1 > score2:
    print("Player 1 wins!")
  else:
    print("Player 2 wins!")
#----------------------------Milestone #3----------------------------
def milestone3(num=0,score1=0,score2=0,turntotal=0,turn=randint(1,2),rollhold=""):
  while score1 < 100 and score2 < 100:
    if turn == 1:
      print("Player 1's turn")
    else:
      print("Computer's turn")
    while num != 1 and (turntotal < 15 if turn == 2 else turntotal < 100) and turntotal + (score1 if turn==1 else score2) < 100 and rollhold != "n": #If it's the computer's turn, it will automatically end the turn when it has 15 or more points scored that turn (15 seemed to work slightly better than 20). If it's the player's turn, it will only end automatically if it gets 100 points that turn. The condition following it works the same as milestone 2 to check that the sum of the turn total and x player's score < 100. rollhold is here too which checks if it's n, in which case it will finish the turn and move on to the next player
      rollhold = (input("Would you like to roll? (y/n) ").lower() if turn == 1 else "y") #Allows an input to be made for player 1 (that isn't case sensitive because of .lower()) and automatically chooses roll for the computer.
      while rollhold != "y" and rollhold != "n":
        rollhold = input("Invalid. Try again: ").lower()
      if rollhold == "y":
        num = randint(1,6)
        if num == 1:
          turntotal = 0
        else:
          turntotal += num
        print("Die roll: " + str(num) + "\nTurn total so far: " + str(turntotal))
    print("Turn total: " + str(turntotal))
    if turn == 1:
      score1 += turntotal
      print("Score: " + str(score1))
    else:
      score2 += turntotal
      print("Score: " + str(score2))
    turntotal = 0
    num = 0
    turn = 3 - turn
    rollhold = ""
  if score1 > score2:
    print("Player 1 wins!")
  else:
    print("Computer wins!")
#--------------------------------------------------------
print("-------------Milestone #1-------------")
milestone1()
print("-------------Milestone #2-------------")
milestone2()
print("-------------Milestone #3-------------")
milestone3()