import itertools
from typing import List

def permute(nums):
    return list(itertools.permutations(nums))

# 입력
num = [1,2,3]

# 출력
print(permute(num))