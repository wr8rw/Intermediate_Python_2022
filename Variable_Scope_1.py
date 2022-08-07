#Author:  R. Webster, Optum Technology  1 August 2022
#Purpose:  Python Mentoring
#This module illustrates how to:
# understand variables and the scope of reference

import varmod

def plus_two(num):
  two_more = num + 2
  return two_more

def times_five(num):
  five_times = num * 5
  return five_times

print(plus_two(times_five(5)))

print(five_times) 
