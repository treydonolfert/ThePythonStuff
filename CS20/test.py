from random import randint

def roll():
  return randint(1,6)

turn = 1
score1 = 0
score2 = 0
while score1 < 100 and score2 < 100:
  print("Player " + str(turn) + "'s turn")
  turntotal = 0
  num = roll()
  while num != 1 and turntotal + (score1 if turn==1 else score2) < 100:
    if num == 1:
      turntotal = 0
      break
    turntotal += num
    num = roll()
    print("Die roll: " + str(num) + "\nTurn total so far: " + str(turntotal))
  if turn==1:
    score1 += turntotal
    print("Player 1 Turn total: " + str(turntotal))
    print("Player 1 Score: " + str(score1))
  else:
    score2 += turntotal
    print("Player 2 Turn total: " + str(turntotal))
    print("Player 2 Score: " + str(score2))
  turn = 3 - turn
if score1 > score2:
  print("Player 1 wins!")
else:
  print("Player 2 wins!")

