
"""
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""

def twoSum(nums, target):

    for i in range(len(nums)):       
        for j in range(len(nums)):
            if i == j:
                continue
            if nums[i] + nums[j] == target:
                return [i, j]



nums = [2,7,11,15]
target = 13

res = twoSum(nums, target)
print(res)

