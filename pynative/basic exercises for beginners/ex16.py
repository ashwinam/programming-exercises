"""Numerical Paliandrome check"""

"""Write a program to check if a given number is a paliandrome (reads the same forward and backward)

Using math
number = 121
number%10 will return single characters reversly

for combination formula is
initialize variable with 0 and (variable * 10) + quotient
"""

given_number = 121

def paliandrome(number):
    original_number = number
    reversed_number = 0
    
    while number:
        quotient = number % 10
        number = number // 10

        reversed_number = (reversed_number * 10) + quotient

    return original_number == reversed_number

print(paliandrome(given_number))