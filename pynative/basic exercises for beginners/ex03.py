"""String Indexing and Even Slicing"""

"""Display only those characters which are present at an even index number in given string.

pseudocode

BEGIN
GIVEN STRING "PYNATIVE"
FOR INDEX IN PYNATIVE.LENGTH:
    IF INDEX IS DIVISIBLE BY 2:
        PRINT STRING[INDEX]

END 
"""

given_string = 'pynative'

print(f'Original String is {given_string}')
print('Printing only even indexes')
for index in range(len(given_string)):
    if index % 2 == 0:
        print(given_string[index])
