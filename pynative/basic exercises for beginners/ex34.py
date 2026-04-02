"""Print reverse number pattern"""

"""Print a downward number pattern where each row starts with a decreasing value"""

row = 5

for row_count in range(row):
    for column in range(row - row_count, 0, -1):
        print(column, end=" ")
    print()