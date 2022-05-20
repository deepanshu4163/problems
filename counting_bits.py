
"""

    Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), 
    ans[i] is the number of 1's in the binary representation of i.

    Example ->

    Input: n = 5
    Output: [0,1,1,2,1,2]
    Explanation:
            0 --> 0
            1 --> 1
            2 --> 10
            3 --> 11
            4 --> 100
            5 --> 101

"""


def DecimalToBinary(num):
    return "{0:b}".format(int(num))

def NumberOfOnes(num):
    count = 0
    for i in range(len(num)):
        if num[i] == '1':
            count = count + 1
    return count


def CountingBits(n):
    ans = []
    for i in range(n + 1):
        num = DecimalToBinary(i)
        ones = NumberOfOnes(num)
        ans.append(ones)
    return ans    


ans = CountingBits(5)

print(ans)