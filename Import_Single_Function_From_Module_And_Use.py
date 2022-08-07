#Author:  R. Webster, Optum Technology  1 August 2022
#Purpose:  Python Mentoring
#This module illustrates how to:
# import a single function from a module AND
# call the reusable function from inside the importing file

#importing a specific function from module fibo
from fibo import fib

fib_input = 10

print("Printing a Fibonacci series up to " + str(fib_input))
fib(fib_input)

