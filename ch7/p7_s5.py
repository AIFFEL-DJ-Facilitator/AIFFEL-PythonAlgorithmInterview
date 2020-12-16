"""
5번 방법을 적용한 풀이입니다.
"""

nums = [11, 2,7,15]

def func(nums, target):
    num_dic = dict()
    for i, num in enumerate(nums): # index를 기록하기 위해 index와 value을 dictionary로 만들어 줍니다. 키 값에 index가 아닌 value를 넣어도 무방합니다만 이 경우 약간의 코드를 수정해야합니다.
        num_dic[i] = num
    num_dic = sorted(num_dic.items(), key=lambda x: x[1]) # 5번 풀이 방식을 위해 정렬해줍니다.
    
    left = 0
    right = len(nums) -1
    
    while not left == right:
        if num_dic[left][1] + num_dic[right][1] < target:
            left += 1
        elif num_dic[left][1] + num_dic[right][1] > target:
            right += -1
        else:
            return num_dic[left][0], num_dic[right][0]

func(nums, target)