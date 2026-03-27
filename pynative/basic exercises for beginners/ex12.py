"""List Comparison and boolean logic"""

"""Write a function to return True if the first and last number of a given list is the same. if the numbers are different return False

pseudocode
BEGIN

INPUT X
INPUT Y

IF X[-1] == Y[-1]:
    RETURN TRUE
ELSE
    RETURN FALSE
"""

def comparing_list(list_x):
    return list_x[0] == list_x[-1]

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

result = comparing_list(numbers_x)

print(f'The Result are :{result}')

result = comparing_list(numbers_y)
print(f'The Result are :{result}')

