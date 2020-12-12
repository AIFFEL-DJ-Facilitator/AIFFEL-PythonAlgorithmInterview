#nums = [2,7,11,15], target = 9
def solution(nums, target):
    nums_map = {}

    for i, num in enumerate(nums):
        if target - num in nums_map: #선 조건 확인
            return [nums_map[target - num], i]
        nums_map[num] = i # 후 딕셔너리 생성하기