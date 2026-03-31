"""Generate fibonacci series"""

"""Write a program to print the first 15 terms of the Fibonacci series. The sequence start with 0 and 1, and each subsequent number is the sum of two preceding number

terms = 15

0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
pre 0
curr 1
next 1
"""

terms = 15

num1, num2 = 0, 1

for i in range(terms):
    print(num1, end=" ")

    # calculate next term
    res = num1 + num2

    # swap the variables
    num1 = num2
    num2 = res

