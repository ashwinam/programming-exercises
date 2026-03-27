"""Removing Duplicates from a list."""

"""Write a list that takes a list containing duplicate items
and returns a new list with only unique elements."""

data = [1, 2, 2, 3, 4, 4, 4, 5]

unique_data = list(set(data))

print(unique_data)