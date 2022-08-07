#Author:  R. Webster, Optum Technology  1 August 2022
#Purpose:  Python Mentoring
#This module illustrates:
# variable definitions and casting

def float_converter(some_float):
#if some_float has a remainder return the original float
#else return the some_float as an int

#test our function:
expecting_float = float_converter(7/3)
expecting_int = float_converter(4/2)

test1 = expecting_float == 7/3 
test2 = expecting_int == 2 and type(expecting_int) == int
test3 = expecting_float != 2

if test1 and test2:
  print("Congrats! You've properly implemented the float_converter function!")
elif test1:
  print("It looks like you've properly returned the original float, but didn't return some_float as an integer when there's no remainder.")
elif test2 and test3:
    print("It looks like you've properly type returned some_float as an integer when there's no remainder! But you still need to return the original float when there is a remainder.")
elif test2 and not test3:
  print("It looks It looks like you may always be returning my_float as an integer regardless of whether or not there's a remainder.")
else: 
  print("It looks like you haven't properly implemented either of the requirements for float_converter.")
