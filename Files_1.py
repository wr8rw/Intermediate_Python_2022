#Author:  R. Webster, Optum Technology  1 August 2022
#Purpose:  Python Mentoring
#This module illustrates how to:
# open a file and perform some functions against the file

#open up a copy of Edgar Allen Poe's The Raven
f = open("/Users/rwebst1/Downloads/The_Raven.txt","r")

### Let's take all the lines in The Raven and store them in a list!

lines = f.readlines()

### Close the file
f.close()
