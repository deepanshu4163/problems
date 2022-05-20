"""
    Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with 6 places after the decimal.

    Example-
        arr = [1, 1, 0, -1, -1]
        There are 5 elements, two positive, two negative and one zero. Their ratios are 2/5, 2/5 and 1/5. Results are printed as:
            0.400000
            0.400000
            0.200000
"""


def plusMinus(arr):
    count_neg = count_pos = count_zero = 0 

    for i in arr:
        if i < 0:
            count_neg += 1
        elif i > 0:
            count_pos += 1
        else:
            count_zero += 1
        
    print("{:.6f}".format(count_pos / len(arr))) 
    print("{:.6f}".format(count_neg / len(arr)))
    print("{:.6f}".format(count_zero / len(arr)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
