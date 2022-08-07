#Author:  R. Webster, Optum Technology  1 August 2022
#Purpose:  Python Mentoring
#This module illustrates how to:
# create a short list
# demonstrates how to determine what a list element is
# demonstrates how to pop elements and what the end result of a pop() is

#Remember:  lists addressing / indexing begins at 0
my_list=[1,2,3,4,5,6]     

#prints zero-eth value in the list
print("Printing the zero-eth element value in the list")
print(my_list[0]) # prints 1

#prints fifth value in the list
print("Printing the fifth element value in the list")
print(my_list[5]) # prints 6

#pops [removes] the third value in the list
print("Popping the third element from the list and printing that element value")
print(my_list.pop(2)) # removes and prints 3

#print the list following completion of the pop()
print("Printing the list following the third element being popped")
print(my_list) # prints [1,2,4,5,6]


