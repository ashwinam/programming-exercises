"""Nested Loops for Multiplication Table"""

"""Print a multiplication table in a formatted grid
Format:

1 2 3 4 5 6 7 8 9 10
2 4 6 8 10 12 14 16 18 20

pseudocode

BEGIN
TABLE_RANGE = 1, 10

FOR ROW IN TABLE_RANGE:
    FOR COLUMN IN TABLE_RANGE:
        PRINT ROW * COLUMN, END=" "
    PRINT FOR NEW LINE

END
"""

table_range = range(1, 11)

for row in table_range:
    for column in table_range:
        print(f'{row * column}', end=" ")

    print()

