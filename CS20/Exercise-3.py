#Treydon Olfert
#October 17th, 2022
#Functions Exercise
#Computer Science 20
#-------------------------------------------------------------------------------------------
#Add Tax:
def calculateprice(price, GST, PST):
  print("Your total price is $" + str(round(price * (GST + PST + 1), 2))) #Prints total price and rounds to the nearest hundredth
calculateprice(float(input("Insert price: ")), float(input("Insert GST rate: ")), float(input("Insert PST rate: "))) #Asks for 3 inputs that are used for price, GST, and PST. GST and PST are assumed to be in decimal form, so 6% GST is 0.06.
#-------------------------------------------------------------------------------------------
#Insert Word:
def insert_word(outside, inside):
  return outside[0:2] + inside + outside[2:4] #Puts 1st and 2nd character first, then puts the inside word, then puts 3rd and 4th characters.
print(insert_word(input("What 4 characters do you want on the outside: "), input("What do you want on the inside: "))) #Asks for 2 inputs from the user, the outside word/characters, and the inside word/characters.
#-------------------------------------------------------------------------------------------
#Triple End:
def triple_end(word):
  return word[-2:] * 3 #Using negative makes it loop to the last letter, so negative 2 is the 2nd last letter and no numbers just makes it go to the end so it'll give the 2nd last and last letter. Multiplying strings just adds multiplicand more strings so *3 gives us our triple ending. 
print(triple_end(input("Type a word: ")))
#-------------------------------------------------------------------------------------------
#Take Two:
def take_two(word):
  return word[2:len(word)] + word[0:2] #Returns the word starting from the 3rd character and to the end of the word, then adds the first 2 characters at the end.
print(take_two(input("Type a word: ")))
#-------------------------------------------------------------------------------------------
#Hotdogs:
def hotdogs(hotdogs, buns):
  if hotdogs > buns: #Since it takes 1 hotdog and 1 bun to make 1 made_hotdogs, the amount of hotdogs we can make will be the same as the smaller variable. In this case, our made_hotdogs will be the same as buns since buns is smaller. 
    made_hotdogs = buns
    remaining_hotdogs = hotdogs - made_hotdogs #The remaining_hotdogs is the difference of our original hotdogs value from made_hotdogs
    remaining_buns = 0 #remaining_buns will be 0 because it was the smaller variable and all the buns were used
  else: #In this case, hotdogs is either less than or equal to buns.
    made_hotdogs = hotdogs #Same logic applies where the smaller variable will equal the made_hotdogs. If the variables equal each other then it won't matter, it'll be 0.
    remaining_buns = buns - made_hotdogs #remaining_buns is the difference of the original buns value from the made_hotdogs. Works if hotdogs == buns too since it'll be 0. 
    remaining_hotdogs = 0 #remaining_hotdogs will be 0 because they were all used. Same applies if hotdogs == buns
  print("You will be able to make " + str(made_hotdogs) + " hotdogs and you will have " + str(remaining_hotdogs) + " hotdogs remaining and " + str(remaining_buns) + " buns remaining.") #Prints all of it together
hotdogs(int(input("How many hotdog packs will there be: ")) * 12, int(input("How many bun packs will there be: ")) * 8) #Asks for 2 inputs that are multiplied to equal how many hotdogs and buns there are