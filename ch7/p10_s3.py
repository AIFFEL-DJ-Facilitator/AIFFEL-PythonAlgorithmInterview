def arrayPairSum(nums):
    return sum(sorted(nums)[::2])
    # 2번째 솔루션과 동일함

# 입력
nums = [1,4,3,2]


# 출력
print(arrayPairSum(nums))