#Author:  R. Webster, Optum Technology  7 August 2022
#Purpose:  Python Mentoring
#This module illustrates:
# How to determine if an input string is a valid url OR not.
# This uses a called function named isValidURL.


import re

def isValidURL(str):
 
    # Regex to check valid URL
    regex = ("((http|https)://)(www.)?" +
             "[a-zA-Z0-9@:%._\\+~#?&//=]" +
             "{2,256}\\.[a-z]" +
             "{2,6}\\b([-a-zA-Z0-9@:%" +
             "._\\+~#?&//=]*)")
     
    # Compile the ReGex
    p = re.compile(regex)
 
    # If the string is empty
    # return false
    if (str == None):
        return False
 
    # Return if the string
    # matched the ReGex
    if(re.search(p, str)):
        return True
    else:
        return False
 
# Driver code
 
# Test Case:
input_url = input("Give me a weel formed web address gunky:  ")

while input_url != 'done':
 if(isValidURL(input_url) == True):
    print("Yes - this is a real URL")
 else:
    print("You have to be kidding me, ha ha ha !")
 input_url = input("Give me a well formed web address gunky: ")

print("Outta here...See ya later 'gator  ")
    
