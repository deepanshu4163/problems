"""
    Full Pyramid Pattern using numbers
"""

for i in range(5):
    for k in range(4 - i):
        print(" ", end="")
    for j in range(1, i + 2):
        print(j, end="")
    for l in range(1, i + 1):
        print(l, end="")
    print()