#nums = [2,7,11,15], target = 9

def solution(nums, target):
    for i in range(len(nums)): #i = [0 : 4)
        for j in range(i+1, len(nums)): # j = s[1: 4), [2, 4), [3, 4)
            if nums[i] + nums[j] == target: #[0, 1]
                return [i, j]