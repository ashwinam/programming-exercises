"""Arithmetic product and conditional logic"""

"""Write a Python function that accepts two integer numbers. If the product of the two numbers is less than or equal to 1000, return their product; otherwise, return their sum."""

number_1 = 50
number_2 = 50

if number_1 * number_2 <= 1_000:
    print(number_1 * number_2)
else:
    print(number_1 + number_2)