"""
    Inverted Full Pyramid Pattern
"""


for i in range(5):
    for j in range(i):
        print(" ", end="")
    for k in range(5 - i):
        print("*", end="")
    for l in range(4 - i):
        print("*", end="")
    print()