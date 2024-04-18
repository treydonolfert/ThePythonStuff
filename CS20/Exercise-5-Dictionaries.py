#Treydon Olfert
#December 20th, 2022
#Exercise #5 - Dictionaries
#Computer Science 20
#--------------------------------------------------------------------------------------
#Movie Reviews
reviews = {"Morbius" : 0, "Avengers: Infinity War": 5, "Avengers: Endgame": 4, "Spider-Man: No Way Home" : 5}
title = input("Add a movie to our reviews: ")
while title in reviews:
  title = input("We already have that movie. Its rating is " + str(reviews[title]) + "/5. Please try another movie: ")
reviews[title] = int(input("Please give this movie a rating: "))
print(reviews)
#--------------------------------------------------------------------------------------
#Translator
translate = {"hello" : "Hallo", "world" : "Welt", "goodbye" : "Auf Wiedersehen", "day" : "Tag", "night" : "Nacht", "have" : "Habe", "a" : "Ein", "good" : "Gut"}
wordorphrase = input("Pick an English word or sentence to be translated into German: ").lower().split() #all keys in translate are lowercased, so doing .lower() on whatever the input is will let them type without case sensitivity. .split() is used to separate every word they typed into the list wordorphrase
translatedlist = []
for word in wordorphrase:
  if word not in translate:
    addword = input("A word you entered, \"" + word + "\", is not in the translator. Would you like to add the translation for this? (Y/N) ")
    if addword.lower() == "y":
      translate[word] = input("Please enter the translation: ")
    else:
      print("Terminating translation.")
      break
  translatedlist.append(translate[word])
if len(wordorphrase) == len(translatedlist): #they should have the same length unless the translation was interrupted, which happens when they don't want to add a translation.
  print(" ".join(translatedlist)) #puts all the words together and separates them with a space
print("The words that can be translated are: " + ", ".join(translate.keys())) #.keys() takes all of the keys (which are the English words). ", ".join() is used to combine them all and, separate, them, like, this
#--------------------------------------------------------------------------------------
#Character Count
def charactercount(string):
  counter = {}
  list = []
  list.extend(string) #extend makes every character of string a separate index in list
  for character in list:
    if character in counter:
      counter[character] += 1
    else:
      counter[character] = 1
  return counter
print(charactercount(input("Type a string: ")))