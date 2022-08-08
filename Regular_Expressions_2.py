#Author:  R. Webster, Optum Technology  7 August 2022
#Purpose:  Python Mentoring
#This module illustrates:
# An initial search using regular expressions
# In this case the parsing of a string to determine if the e-mail address
#  entry is correctly formatted


import re
my_input = 'a@myco.com'

# check for one or more digits
if re.search('^\w+@\w+\.\w+$', my_input):
  print("E-mail address valid")
else:
  print("Error: Invalid email address!")
