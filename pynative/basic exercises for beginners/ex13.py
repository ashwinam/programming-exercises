"""Filtering List with Conditional Logic"""

"""Iterate through a given list of numbers and print only those numbers which divisible by 5"""

nums = [10, 20, 33, 46, 55]

for num in nums:
    if num % 5 == 0:
        print(num)