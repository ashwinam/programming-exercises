"""String Slicing and Substring Removal"""

"""Write a function to remove characters from a string
starting from index 0 upto n and return a new string"""

def remove_chars(string, index):
    """Return new string by slicing"""

    return string[index:]

print(remove_chars("pynative", 4))
print(remove_chars("pynative", 2))