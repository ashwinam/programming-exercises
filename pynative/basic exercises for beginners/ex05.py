"""Variable Swapping (The In-Place Method)"""

"""Write a program to swap the values of two variables, a and b, without using a third temporary variable"""

a=5
b=10

print(f'Original Values a: {a}, b: {b}')

a, b = b, a

print(f'After Result Values a: {a}, b: {b}')