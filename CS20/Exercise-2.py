#Treydon Olfert
#October 3rd, 2022
#Conditionals & Control Flow Exercise
#Computer Science 20
#-------------------------------------------------------------------------------------------
#Discount:
gadgets = input("How many gadgets would you like to purchase: ")
if gadgets.isdigit(): #Check if it's an integer. You can not buy part of a gadget or a "c" amount of gadgets.
  cost = 4 * int(gadgets) #$4 per gadgets
  if int(gadgets) > 5 and int(gadgets) <= 10: #Check if they bought more than 5, but less than 11, making them eligible for 10% discount.
    final_cost = 0.9 * cost
    money_saved = 0.1 * cost
  elif int(gadgets) > 10: #Check if they bought more than 10 which makes them eligible for 15%  off.
    final_cost = 0.85 * cost
    money_saved = 0.15 * cost
  else: #Otherwise, they bought 5 or less so they get no discount
    final_cost = cost
    money_saved = 0
  print("You bought $" + str(final_cost) + " of gadgets! You saved $" + str(money_saved) + "!")
else: #The input was not an integer.
  print("That's not a valid number!")
#-------------------------------------------------------------------------------------------
#Alarm:
time = input("How many hours from now will the alarm go off: ") #Ask how many hours
if time.isdigit(): #Check if it's an integer
  days = int(time) // 24 #24 hours in a day, rounds down.
  time = int(time) % 24 + 2 #This will give what time in a 24 hour clock...
  if time >= 12 and time <= 23: #...now we check if it's am or pm
    am_or_pm = "AM"
  else:
    am_or_pm = "PM"
  time %= 12 #Then we convert the time into a 12 hour clock
  if time == 0: #Before line 32, if time equaled 12 then now it will equal 0 since the remainder of 12/12 and 24/12 will be 0. 0PM/AM doesn't make much sense, so if time is 0, we set it to 12.
    time = 12
  if days == 1: #Saying 1 days is grammatically incorrect, so check if days == 1 and if it does, make it day instead of days
    single_or_plural = " day"
  else:
    single_or_plural = " days"
  print("Your alarm will go off in " + str(days) + single_or_plural + " at " + str(time) + am_or_pm) #Print it all
else: #The input was not an integer.
  print("Not a valid number of hours!")