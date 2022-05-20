def findMedian(arr):
    sorted_arr = sorted(arr)
    middle = len(arr) // 2
    print(sorted_arr)
    return sorted_arr[middle]

print(findMedian([5, 3, 4, 1, 2, 7 , 0, 9]))