"""
    You are asked to ensure that the first and last names of people begin with a capital letter in their passports. 
    For example, alison heck should be capitalised correctly as Alison Heck.
"""

def solve(s):
    r = ""
    for i in range(len(s)):
        if i == 0:
            r += s[i].capitalize()
        elif s[i - 1] == " ":
            r += s[i].capitalize()
        else:
            r += s[i]    
        
    return r

if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)

#OR
# def solve(s):
#     res_list = s.split()
#     for i in range(len(res_list)):
#         res_list[i] = res_list[i].capitalize()
        
#     return " ".join(res_list)