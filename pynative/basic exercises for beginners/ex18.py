"""Integer Digit Extraction and reversal."""

"""Write a program to extract each digit from an integer in the reverse order


pseudocode
BEGIN

NUMBER ASSIGN AN INPUT VALUE AS INTEGER
REVERSE_DIGIT = 0
WHILE NUMBER:
    DIGIT = NUMBER % 10
    NUMBER = NUMBER // 10
    REVERSE_DIGIT = (REVERSE_DIGIT * 10) + DIGIT

PRINT REVERSE_DIGIT

END
"""

def rever_digit(number):
    reverse_digit = 0

    while number:
        digit = number % 10
        number = number // 10

        reverse_digit = (reverse_digit * 10) + digit

    return reverse_digit

result = rever_digit(7536)

print(result)
