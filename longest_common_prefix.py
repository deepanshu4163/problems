"""
    Write a function to find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string "".
"""

strs = ["flower","flow","flight"]
# strs = ["dog","racecar","car"]


longPref = strs[0]
    
for string in strs:
    for index in range(0, len(longPref)):
        if (index >= len(string) or longPref[index] != string[index]):
            longPref = longPref[0:index]
            break   

print(longPref)
