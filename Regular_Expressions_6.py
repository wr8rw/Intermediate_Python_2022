#Author:  R. Webster, Optum Technology  7 August 2022
#Purpose:  Python Mentoring
#This module illustrates:
# How to determine if an input string is a valid US phone number OR not.
# This uses a called function named isValid.

import re
  
def isValid(s):
      
    # 1) Begins with three digit area code surrounded by parenthesis
    # 2) Then a space
    # 3) Then three digit "exchange"
    # 4) Then a hyphen or dash
    # 5) Then four digit "extension"
    Pattern = re.compile("\(\w{3}\) \w{3}-\w{4}")
    return Pattern.match(s)
  
# Driver Code
phone_number = input("How's about a phone number for me:  ")
while phone_number != 'done':
  if (isValid(phone_number)): 
    print (phone_number + " Valid Number")     
  else :
    print (phone_number + " Invalid Number...you've got a problem") 
  phone_number = input("How's about a phone number for me:  ")
