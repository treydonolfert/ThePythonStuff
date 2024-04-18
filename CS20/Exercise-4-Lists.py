#Treydon Olfert
#December 15th, 2022
#Exercise #4 - Lists
#Computer Science 20
#-------------------------------------------------------------------------------
#Make List
animals = [input("Type the names of 5 animals: "), input("Type the names of 4 more animals: "), input("Type the names of 3 more animals: "), input("Type the names of 2 more animals: "), input("Type the name of 1 more animal: ")] #Combines the list and the inputs into one line.
indexnum = int(input("Type a number from 1 to 5: "))
animals.pop(indexnum-1)
indexnum = int(input("Type a number from 1 to 4: "))
animals.pop(indexnum-1)
print("The remaining animals are " + animals[0] + ", " + animals[1] + ", and " + animals[2])
#-------------------------------------------------------------------------------
#avg()
def avg(numbers):
  if len(numbers): #len() returns True when > 0. When it's 0, it'll return False.
    return round(sum(numbers)/len(numbers), 1) #sum adds everything together in a list
  else:
    return "No numbers."
print(avg([4,6,7,3,2,1]))
print(avg([1]))
print(avg([]))
#-------------------------------------------------------------------------------
#Unlucky Number 7
def unlucky_number_7(numbers2):
  sum = 0
  for number in numbers2:
    if number == 7:
      break
    else:
      sum += number
  return sum
print(unlucky_number_7([7,5,4,2]))
print(unlucky_number_7([6,7,4,2,3,2]))
print(unlucky_number_7([6,5,7,2]))
print(unlucky_number_7([6,5,4,2,-2]))
#-------------------------------------------------------------------------------
#remove_duplicates()
def remove_duplicates(numbers3):
  noduplicatelist = [] 
  for value in numbers3:
    if value not in noduplicatelist:
      noduplicatelist.append(value) #Adds to noduplicatelist with something that's not already in the list.
  return noduplicatelist
print(remove_duplicates([3,4,6,3,2,1,3,4,3,3,7,6,4]))
print (remove_duplicates([]))
print (remove_duplicates([2,3,1]))
print(remove_duplicates(['red','pink','blue','red','blue']))
#-------------------------------------------------------------------------------
#mode()
def mode(my_list):
  modelist = []
  count = 0
  for value in my_list: #Looks through every value in the list.
    if value not in modelist: #If it's already in the list it skips since it's already known that that value is a mode, at least for now.
      if my_list.count(value) > count:
        modelist = [value] #The value was bigger than the previous mode(s), so it replaces it.
        count = my_list.count(value)
      elif my_list.count(value) == count:
        modelist.append(value) #The value was the same as the previous mode, so it is also a mode.
  if count == 1 or count == 0: #This is run when either no numbers repeat or there's no numbers. 
    return "No mode!"
  else:
    return modelist
print(mode([3,4,5,4,3,5,3,3,3,3]))
print(mode([2,3,2,4,3]))
print(mode([1,2,5,2,5,2,7,7,5,5,5,2,2]))
print(mode([1,8,7,2,3,5]))
print(mode([2]))
print(mode([]))
