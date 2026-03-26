"""Vowel frequency conter"""

"""Write a program to count the total number of vowels(a,e,i,o,u) present in the given sentence

pseudocode
BEGIN
VOWEL_COUNT = 0
FOR EACH_CHAR IN INPUT:
    IF EACH_CHAR IN "AEIOU":
        VOWEL_COUNT INCREMENT BY 1

PRINT VOWEL_COUNT

END
"""

sentence = "Learning Python is fun!"
vowel_count = 0

for each_char in sentence:
    if each_char in "aeiou":
        vowel_count += 1

print(vowel_count)

