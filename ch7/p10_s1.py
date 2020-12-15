def arrayPairSum(nums):
    sum = 0
    pair = []
    nums.sort()

    for n in nums:
        pair.append(n)
        if len(pair) == 2: # 페어가 맞는지 확인
            sum += min(pair) # 2개의 값 중 작은 값을 더함
            pair = [] # 다음 페어를 만들기 위해 초기화

    return sum

# 입력
nums = [1,4,3,2]


# 출력
print(arrayPairSum(nums))