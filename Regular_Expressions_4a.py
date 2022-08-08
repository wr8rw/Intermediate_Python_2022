#Author:  R. Webster, Optum Technology  7 August 2022
#Purpose:  Python Mentoring
#This module illustrates:
# How to determine if input is a number or not.
# This uses a called function named is_numeric.


def is_numeric(val):
	if str(val).isdigit():
		return True
	elif str(val).replace('.','',1).isdigit():
		return True
	else:
		return False


something = " "
while something != 'done':
 something = input("Give me a number boss: ")
 print(is_numeric(something))

  
