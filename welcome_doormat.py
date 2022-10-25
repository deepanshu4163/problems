"""
    Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
"""
N = int(input())
M = N * 3

for i in range(N):
    if i % 2 != 0:
        print("-" * int((M - 3 * i) / 2) + ".|." * (i) + "-" * int((M - 3 * i) / 2))

print("WELCOME".center(M, "-"))

for i in range(N - 1, 0, -1):
    if i % 2 != 0:
        print("-" * int((M - 3 * i) / 2) + ".|." * (i) + "-" * int((M - 3 * i) / 2))



#OR
# nm = list(map(int, input().split()))
# n = nm[0]
# m = nm[1]

# for row in range(n//2):
#     print(('.|.'*(row*2+1)).center(m, '-'))
    
# print('WELCOME'.center(m, '-'))
    
# for row in range(n//2, 0, -1):
#     print(('.|.'*(row*2-1)).center(m, '-'))