# This module illustrates a basic dictionary, how it is accessed, and what can be done with the returned information

my_dict = {"dictionary" : "a book or electronic resource that lists the words of a language",\
           "int" : "short for integer. A whole number; a number that is not a fraction",\
           "float" : "for our purposes this means a decimal number— a number that consists of a whole number and a fractional part",\
           "bool" : "short for boolean; a binary, True or False value"}

if 'tuple' in my_dict:
  print("'tuple' is a key in my_dict")
else:
  print("'tuple' is NOT a key in my_dict")

if 'int' in my_dict:
  print("'int' is a key in my_dict")
else:
  print("'int' is NOT a key in my_dict")
