"""
    Given an integer, n , print the following values for each integer i from 1 to n:

    1.Decimal
    2.Octal
    3.Hexadecimal (capitalized)
    4.Binary
"""


def print_formatted(number):
    width = len(bin(number)[2:])
    for i in range(1, number + 1):
        b = str(bin(i)[2:])
        o = str(oct(i)[2:])
        h = str(hex(i)[2:]).upper()
        print(str(i).rjust(width), o.rjust(width), h.rjust(width), b.rjust(width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)