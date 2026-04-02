"""Print Alternate Prime Numbers"""

"""Write a program to find all prime numbers up to 20, but only print every second(alternate) prime number found"""

def is_prime(number):
    """Find out prime"""
    prime = False
    for i in range(2, number):
        if number % i == 0:
            prime = False
            break
    else:
        prime = True
    
    return prime

print(2, end=" ")
position = 0
for i in range(1, 20):
    if i > 2:
        if is_prime(i):
            position += 1
            if position % 2 == 0:
                print(i, end=" ")


