"""Odd/Even List Splitter"""
numbers = [12, 7, 34, 21, 5, 10, 8, 3, 19, 2]

odd = []
even = []

for number in numbers:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

print(odd)
print(even)