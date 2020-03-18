# Jina Kim
# Run a few regular expression

import regex

#Take infix regular expression from the user
regexes=input("Enter your value : ")

#Take the string that the user wants to match
stringToMatch=input("Enter the string that you want to match : ")

#To print the result as True or False
print("The result is", regex.match(regexes,stringToMatch))
