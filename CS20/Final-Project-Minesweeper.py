#Final Project - Minesweeper
#Treydon Olfert
#Computer Science 20
#January 27th, 2023
import random

firstmove = True
board = [[' ' for i in range(8)] for i in range(8)] #Makes a list of 8 lists with 8 strings that are just a space.
actualboard = [[' ' for i in range(8)] for i in range(8)] #Makes a duplicate. Throughout the code, actualboard is what the player sees and board is the internal board that has all mines marked and what numbers are on what tiles.
visited = [[False for i in range(8)] for i in range(8)] #Makes a list the same way as board but it's all False instead of space strings. 
mines = random.sample(range(64), 10) #Makes a list of 10 random numbers that go from 0-63. These are the mines. 
letterstonumbers = {"a" : 0, "b" : 1, "c" : 2, "d" : 3, "e" : 4, "f" : 5, "g" : 6, "h" : 7} #Dictionary made to translate the lettered coordinates typed by the user into coordinates that can be used for board and actualboard

def printboard():
  print("    1   2   3   4   5   6   7   8")
  for i, row in enumerate(actualboard): #enumerate is used here to count how many times the loop has gone through and is kept track of in i. 
    print(chr(i+97) + " |", end="") #chr turns numbers into their unicode characters, this is used with enumerate to efficiently show a-h on the board. end = "" is also used here so that the different print statements will print on the same line instead of going to a new line.
    for tile in row:
      print(" " + str(tile) + " |", end = "")
    print("\n", end="")
    
def checkadjacenttiles(x,y): #Checks all adjacent tiles using nested for loops. This is used throughout the program.
  for i in range(x-1, x+2):
    for j in range(y-1, y+2):
      if i >= 0 and i < 8 and j >= 0 and j < 8: #Checks if the adjacent coordinates are actually on the grid
        if board[i][j] == '9':
          board[x][y] = str(int(board[x][y]) + 1) if board[x][y] != " " else "1" #Adds +1 to the adjacent tile. This is how the numbers that are adjacent to the bombs are made.

def adjacentclearing(x,y): #Adjacent clearing automatically clears tiles adjacent to a tile that is uncovered and has no adjacent bombs (represented with a 0 on actualboard and a space on board). It is also used on the first move regardless of whether or not the tile uncovered had adjacent bombs so it's easier to start.
  if visited[x][y] == True:
    return
  visited[x][y] = True #Visited is used here to make sure the function doesn't keep infinitely repeating and stops once it sees a tile it's already been at.
  for i in range(x-1, x+2):
    for j in range(y-1, y+2):
      if i >= 0 and i < 8 and j >= 0 and j < 8:
        if board[i][j] != '9':
          actualboard[i][j] = board[i][j] if board[i][j] != " " else "0" #Uncovers it unless it's a space, in which case it will be displayed as a 0 since every uncovered tile is already blank in actualboard.
          if board[i][j] == ' ':
            adjacentclearing(i, j) #Clears again if the newly uncovered tile had no adjacent bombs.

for mine in mines:
  x = mine // 8
  y = mine % 8 #Turns the randomly chosen mine numbers into coordinates and then marks them as 9's on board (since 9's are impossible to get)
  board[x][y] = '9'

for x in range(8):
  for y in range(8):
    if board[x][y] != '9':
      checkadjacenttiles(x, y)
        
printboard()

while True:
  x = input("What lettered coordinate would you like to uncover? ").lower()
  while x != "a" and x != "b" and x != "c" and x != "d" and x != "e" and x != "f" and x != "g" and x != "h":
    x = input("Invalid. Try again: ").lower()
  x = letterstonumbers[x]
  y = input("What numbered coordinate would you like to uncover? ")
  while y != '1' and y != '2' and y != '3' and y != '4' and y != '5' and y != '6' and y != '7' and y != '8':
    y = input("Invalid. Try again: ")
  y = int(y) - 1 #Turns what they typed into coordinates that can be used on board and actualboard
  if firstmove == True:
    while board[x][y] == '9':
      x = input("Your first pick was a mine! Pick another lettered coordinate: ").lower()
      while x != "a" and x != "b" and x != "c" and x != "d" and x != "e" and x != "f" and x != "g" and x != "h":
        x = input("Invalid. Try again: ").lower()
      x = letterstonumbers[x]
      y = input("Pick another numbered coordinate: ")
      while y != '1' and y != '2' and y != '3' and y != '4' and y != '5' and y != '6' and y != '7' and y != '8':
        y = input("Invalid. Try again: ")
      y = int(y) - 1
    adjacentclearing(x,y)
    firstmove = False
  if board[x][y] == '9':
    print("You picked a mine! You lost!")
    break
  actualboard[x][y] = board[x][y] if board[x][y] != ' ' else '0'
  if actualboard[x][y] == '0':
    adjacentclearing(x,y)
  printboard()
  if sum([1 for row in actualboard for tile in row if tile == " "]) == 10: #Counts each tile in actualboard that has not been uncovered after every turn to see if it equals the number of mines (10). If it is, the game is won.  
   print("You uncovered all tiles and avoided the mines! You won!")
   break