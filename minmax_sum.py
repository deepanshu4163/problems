"""
    Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

    Example: arr = [1, 3, 5, 7, 9]

        The minimum sum is 1 + 3 + 5 + 7 = 16 and the maximum sum is 3 + 5 + 7 + 9 = 24. The function prints
"""


def miniMaxSum(arr):
    
    itr = 0
    max = 0
    min = sum(arr)
    while itr < 5:
        sum_arr = 0
        for i in range(len(arr)):
            if i == itr:
                continue
            sum_arr += arr[i]
        itr += 1 
        if sum_arr > max:
            max = sum_arr
        if sum_arr < min:
            min = sum_arr 

    print(min, max)           

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
