#Author:  R. Webster, Optum Technology  1 August 2022
#Purpose:  Python Mentoring
#This module illustrates how to:
# open a file and perform some functions against the file
# then write out the file as lower case

f = open("/Users/rwebst1/Downloads/The_Raven.txt", "r") #open Moby-Dick file
lines = f.readlines() #put all lines from Moby-Dick into a list
f.close() #close the file

new_file = open("/Users/rwebst1/Downloads/The_Raven_lowercase.txt", "w") #write new file to Documents folder

for line in lines:
    new_file.write(line.lower())

new_file.close()
