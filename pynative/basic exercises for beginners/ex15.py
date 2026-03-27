"""Nested Loops for pattern Generation"""

"""Print a the following pattern where each row contains a number repeated a spcific number of times based on its value

Pattern:
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5

pseudocode
BEGIN

# OUTER LOOP PRINTS ROW
# INNER LOOP PRINTS COLUMN

FOR ROW IN RANGE 1, 6
    FOR COLUMN IN RANGE 0, ROW
        PRINT("*")
    PRINT()

END

DRY-RUN

ROW = 3
COLUMN = 0, 3

*
**
***
****
*****
"""

for row in range(1, 6):
    for column in range(0, row):
        print(row, end=" ")
    print()