"""Finding Common Elements"""

"""Take two list and find the common element that appear in both"""

list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]

list_a = set(list_a)
list_b = set(list_b)

print(list_a & list_b)