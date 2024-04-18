#Treydon Olfert
#September 28th, 2022 
#Strings and Console Ouput Exercise
#Computer Science 20
#------------------------------------------------------------------------------------------
#Famous Quote:
quote = "\"I don't feel guilty for anything. I feel sorry for people who feel guilt.\" " #Using \ before " cancels the "
author = "- Ted Bundy"
print(quote + author)
print(quote + author.upper()) #.upper makes "- Ted Bundy" all caps
#------------------------------------------------------------------------------------------
#First Middle Last:
word = "CRAFT"
middle = int(len(word)/2) #Takes the rounded down value of the length of the word divided by 2. Since Python starts counting from 0, this will give the middle letter in all words with an odd number of letters.
print(word[0] + word[middle] + word[-1]) #word[-1] works because the first letter is 0, so putting -1 will make it loop back to the last letter of the word.
#------------------------------------------------------------------------------------------
#Greeting:
name = "Treydon"
age = int(365.25 * 16)
print("Hi my name is %s. I am %s days old." %(name, age))