def arrayPairSum(nums):
    sum = 0
    nums.sort()

    for i, n in enumerate(nums):
        # i를 인덱스라고 생각하고
        # i를 2로 나누었을 때 0인 인덱스의 요소만 합함
        # ex) i = 0, 2, 4, 6, ......
        if i % 2 == 0:
            sum += n

    return sum

# 입력
nums = [1,4,3,2]


# 출력
print(arrayPairSum(nums))