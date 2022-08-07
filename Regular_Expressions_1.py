#Author:  R. Webster, Optum Technology  1 August 2022
#Purpose:  Python Mentoring
#This module illustrates how to:
# use regular expressions to evaluate an input stream

#import systems module
import re
my_input = input("Give me a series of numbers e.g.'1234'")
while str(my_input) != 'done':

# check to see if there are four consecutive digits somewhere in the input
   digits_test = re.search('\d\d\d\d', my_input)

   if digits_test:
     print("We have four digits!")
   else:
     print("Invalid data")
   my_input = input("Give me a series of comma separated numbers e.g.'1234'")

