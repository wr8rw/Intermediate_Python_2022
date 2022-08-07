#Author:  R. Webster, Optum Technology  1 August 2022
#Purpose:  Python Mentoring
#This module illustrates:
# a program with functions and use of them for a test

#Define the functions
def plus_two(num):
  two_more = num + 2
  return two_more

def times_five(num):
  five_times = num * 5
  return five_times


print(plus_two(times_five(5)))
