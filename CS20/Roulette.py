from random import randint
from collections import Counter
from statistics import multimode, median, fmean, pstdev

barrel = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0}
bullet1 = None
bullet2 = None
movecounter = 1
dead = False
movelist = []
for i in range(2500):
    barrel = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0}
    dead = False
    movecounter = 1
    for m in range(2):
        if m == 0:
            bullet1 = randint(0,5)
        if m == 1:
            bullet2 = randint(0,5)
            while bullet1 == bullet2:
                bullet2 = randint(0,5)
    barrel[bullet1] = 1
    barrel[bullet2] = 1
    currentSelection = randint(0,5)
    #print("2 bullets have been placed into this gun. The computer can decide to spin the barrel or shoot the gun as is.")
    while dead != True:
        currentSelection = randint(0,5)
        if barrel[currentSelection] == 1:
            dead = True
            #print("The computer spun. It did not survive. Lasted " + str(movecounter) + ". Rest in peace...")
            movelist.append(movecounter)
            #print("Game End: #" + str(len(movelist)))
        else:
            #print("The computer spun and shot. It survived. The next turn may commence.")
            movecounter += 1
data = Counter(movelist)
mode = multimode(movelist)
mean = fmean(movelist)
medianv = median(movelist)
standardDeviation = pstdev(movelist)
rangev = max(movelist) - min(movelist)
print("Total runs: " + str(len(movelist)) + "\nHighest: " + str(max(movelist)) + " \nLowest: " + str(min(movelist)) + " \nRange: " + str(rangev) + " \nMean: " + str(mean) + "\nMedian: " + str(medianv) + "\nMode: " + str(mode) + "\nStandard Deviation: " + str(standardDeviation))
for i in range(max(movelist)):
    print(str(i+1) + ": " + str(data[i+1]))