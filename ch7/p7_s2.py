#nums = [2,7,11,15], target = 9
def solution(nums, target):
    for i, j in enumerate(nums): # i = [0, 1, 2, 3], j=[2, 7, 11, 15]
        complement = target - j # complement = [7, 2, -2, -6]
    
    if complement in nums[i+1:]: # nums[i+1] = [7, 11, 15], [11, 15], [15]
        return nums.index(j), nums[i+1:].index(complement) + (i+1)