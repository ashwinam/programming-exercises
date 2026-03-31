"""Generate fibonacci series"""

"""Write a program to print the first 15 terms of the Fibonacci series. The sequence start with 0 and 1, and each subsequent number is the sum of two preceding number

terms = 15

0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
pre 0
curr 1
next 1
"""

terms = 15

pre = 0
curr = 1

print(pre, end=" ")
print(curr, " ")

for i in range(terms - 2):
    next_term = pre + curr
    print(next_term, end=" ")
    pre = curr
    curr = next_term

