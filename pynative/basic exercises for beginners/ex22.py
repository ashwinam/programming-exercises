"""Custom Exponent power"""

"""Write a function called exponent(base, exp) that returns an inreger value of the base raised to the power of the exponent

exponent(2, 5)
2 * 2 * 2 * 2 * 2: 32
"""

def exponent(base, exp):
    value = 1
    for i in range(exp):
        value *= 2
    
    return value

print(exponent(2, 5))