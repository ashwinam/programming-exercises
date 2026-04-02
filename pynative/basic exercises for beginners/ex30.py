"""Word Frequency Counter"""

text = "apple banana apple cherry banana apple"

frequency_counter = {}

for word in text.split(" "):
    if word.strip() in frequency_counter:
        frequency_counter[word.strip()] += 1
    else:
        frequency_counter[word.strip()] = 1

print(frequency_counter)