#nums = [2,7,11,15], target = 9
def solution(nums, target):
    nums_map = {}
    for i, num in enumerate(nums):
        nums_map[num] = i #nums_map  = {2:0, 7:1, 11:2, 15: 3}
    
    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]: #9-2 = 7 & 0 != 1
            return nums.index(num), nums_map[target - num] # 0, 1