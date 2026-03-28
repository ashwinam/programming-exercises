"""Merging list with parity filtering"""

"""Create a new list from given two list such that new list contains odd numbers from the first list and even numbers from the second list

pseudocode
BEGIN

NUMBER1 AS A LIST OF NUMBERS
NUMBER2 AS A LIST OF NUMBERS

NEW_LIST ASSIGN BLANK LIST

FOR EACH_NUMBER IN NUMBER1:
    IF EACH_NUMBER % 2 != 0:
        NEW_LIST.APPEND(EACH_NUMBER)

FOR EACH_NUMBER IN NUMBER2:
    IF EACH_NUMBER % 2 == 0:
        NEW_LIST.APPEND(EACH_NUMBER)

PRINT(NEW_LIST)
"""

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

new_list = []

for each_number in list1:
    if each_number % 2 != 0:
        new_list.append(each_number)

for each_number in list2:
    if each_number % 2 == 0:
        new_list.append(each_number)


print(new_list)