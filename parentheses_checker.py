"""
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    An input string is valid if:

        1. Open brackets must be closed by the same type of brackets.
        2. Open brackets must be closed in the correct order.
        3. Every close bracket has a corresponding open bracket of the same type.
"""

stack = []

brackets = {
        "(": ")", 
        "[": "]", 
        "{": "}"
    }

s = ")[]}"

def parentheses_checker(s):
    for i in s:  
        if i in brackets.keys():
            stack.append(i)
        elif i in brackets.values():
            if not stack or brackets[stack[-1]] != i:
                return False
            else:
                stack.pop()

    return len(stack) == 0
    

print(parentheses_checker(s))