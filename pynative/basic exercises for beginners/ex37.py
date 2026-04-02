"""Simple Countdown Timer"""

"""Create a countdown timer that starts from a given number and counts down to zero using a while loop"""

import time

given_number = 5

while given_number:

    print(given_number, end=" ", flush=True)
    time.sleep(1)
    given_number -= 1

print("Blast off!")