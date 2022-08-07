#Author:  R. Webster, Optum Technology  1 August 2022
#Purpose:  Python Mentoring
#This module illustrates how to create a reusable module that contains functions

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b

    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b

    return result
