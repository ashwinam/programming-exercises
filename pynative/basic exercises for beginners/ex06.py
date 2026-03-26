"""Calculating Factorial with a loop"""

"""Write a program that calculates the factorial of a given number (e.g., 5!) using a for loop

5! = 5 * 4 * 3 * 2 * 1

psuedocode

BEGIN
INPUT FACTORIAL NUMBER 
PREVIOUS NUMBER TO 1
FOR EACH NUMBER IN RANGE OF FACTORIAL NUMBER:
    PREVIOUS NUMBER = PREVIOUS NUMBER * EACH NUMBER

PRINT FACTORIAL FOR FACTORIAL NUMBER IS

END

"""

def factorial_number(number):
    factorial_result = 1
    for each_number in range(number, 0, -1):
        factorial_result *= each_number
    
    print(f'Factorial of {number} is : {factorial_result}')

factorial_number(5)