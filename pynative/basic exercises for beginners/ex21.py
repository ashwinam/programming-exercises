"""Downward Half Pyramid Patter"""

"""Draw a downward half pyramid pattern using (*)

*****
****
***
**
*
"""

for row in range(5):
    for column in range(5 - row, 0, -1):
        print("*", end=" ")
    print()