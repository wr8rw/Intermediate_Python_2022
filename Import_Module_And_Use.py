#Author:  R. Webster, Optum Technology  1 August 2022
#Purpose:  Python Mentoring
#This module illustrates how to:
# import an entire module AND
# call a reusable function from inside the imported module

#importing all functions from module fibo
import fibo

fib_input = 10

print("Printing a Fibonacci series up to " + str(fib_input))
fibo.fib(fib_input)

print("Returning a Fibonacci series up to " + str(fib_input))
res = fibo.fib2(fib_input)
print(res)
