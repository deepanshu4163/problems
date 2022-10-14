"""
    Full Pyramid Pattern
"""

for i in range(5):
    for k in range(4 - i):
        print(" ", end="")
    for j in range(i + 1):
        print("*", end="")
    for l in range(i):
        print("*", end="")
    print()