"""
    print the second largest number in an array
"""


n = int(input())
arr = map(int, input().split())
new_arr = list(arr)

max_element = max(new_arr)

cool = []

for i in new_arr:
    if i != max_element:
        cool.append(i)    
        
cool.sort()        
print(max(cool))

