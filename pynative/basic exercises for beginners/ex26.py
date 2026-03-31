"""Mergin two dictionaries"""

def merge_two_dictionaries(dict1, dict2):
    dict1.update(dict2)
    return dict1

dict1 = {"name": "Alice", "age": 25}
dict2 = {"city": "New York", "job": "Engineer"}

print(merge_two_dictionaries(dict1, dict2))