"""Capitalize First letter(Tital Case)"""

"""Write a program to capitalize the first letter of each word in a given string without using the built-in .title() method"""

text = "hello world from python"

new_text = []

for word in text.split():
    new_text.append(word.capitalize())

print(" ".join(new_text))
