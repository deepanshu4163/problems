"""
    Right Half Pyramid Pattern using *
"""

for i in range(5):
    for k in range(4 - i):
        print(" ", end="")
    for j in range(i + 1):
        print("*", end="")

    print()    