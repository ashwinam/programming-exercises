"""Cumulative Sum of a range"""

"""Iterate through the first 10 numbers (0–9). In each iteration, print the current number, the previous number, and their sum.


pseudocode

BEGIN 
PREVIOUS NUMBER IS 0
FOR CURRENT NUMBER IN RANGE:
    PRINT CURRENT NUMBER AND PREVIOUS NUMBER 
    PREVIOUS NUMBER ASSIGNS CURRENT NUMBER

END
"""

previous_number = 0
for current_number in range(10):
    print(f'Current Number {current_number} Previous Number {previous_number} SUM: {current_number + previous_number}')
    previous_number = current_number
