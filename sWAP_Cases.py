"""
    You are given a string and your task is to swap cases. In other words, 
    convert all lowercase letters to uppercase letters and vice versa.
"""

def swap_case(s):
    new_s = ""          #creating new string 
    for i in s:
        if i.islower():
            new_s = new_s + i.upper()     #appending swapped_case value in new string if case is lower
        elif i.isupper():
            new_s = new_s + i.lower()     #appending swapped_case value in new string if case is upper
        else:
            new_s = new_s + i             #appending swapped_case value in new string if i is not alphabet 
        
    return new_s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

    #using swapcase() method to reverse the cases
    print(s.swapcase())