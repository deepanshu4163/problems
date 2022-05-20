"""
PROBLEM:

    Write a function named collatz() that has one parameter named number . If
    number is even, then collatz() should print number // 2 and return this value.
    If number is odd, then collatz() should print and return 3 * number + 1 .

    FUN FACT:

    Amazingly enough, this sequence actually works for any integer—sooner
    or later, using this sequence, you’ll arrive at 1! Even mathematicians aren’t
    sure why. Your program is exploring what’s called the Collatz sequence, some-
    times called “the simplest impossible math problem.”
"""
import sys

def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1


try:
    number = int(input("enter the integer:"))
except ValueError:          #int() returns ValueError if value other than integer is entered
    print("please enter an integer")
    sys.exit()  #quit the program if value other than integer is entered

r = collatz(number)
print(r)

while r != 1:
    r = collatz(r)
    print(r)
