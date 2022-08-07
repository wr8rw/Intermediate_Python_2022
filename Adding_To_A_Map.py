#Author:  R. Webster, Optum Technology  1 August 2022
#Purpose:  Python Mentoring
#This module illustrates:
# how to add elements to a map and subsequently interrogate the map for values

my_dict = {"dictionary" : "a book or electronic resource that lists the words of a language",\
           "int" : "short for integer. A whole number; a number that is not a fraction",\
           "float" : "for our purposes this means a decimal number— a number that consists of a whole number and a fractional part",\
           "bool" : "short for boolean; a binary, True or False value"}

def add_to_dict(key, value):
    print ("Attempting to add " + key + " into my dictionary")
    if key in my_dict:
     print("Oops " + key + " is already a key in my_dict")
    else:
     my_dict[key]= value
     print("Yes! Added " + key + " into my_dict")     

add_to_dict("int","short for integer. A whole number; a number that is not a fraction")
#This should print "This key is already in the dictionary!"

add_to_dict("tuple","an ordered, immutable list of data / objects")
#This should add the key/value pair to the my_dict dictionary and
# print "This key / value pair has been added to the dictionary"

#Now determine if the new values are actually in the map
if 'tuple' in my_dict:
  print("'tuple' is a key in my_dict")
else:
  print("'tuple' is NOT a key in my_dict")

if 'int' in my_dict:
  print("'int' is a key in my_dict")
else:
  print("'int' is NOT a key in my_dict")
