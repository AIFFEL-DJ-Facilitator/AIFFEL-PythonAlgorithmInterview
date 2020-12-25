'''
37. 부분 집합

모든 부분 집합을 리턴하라.

입력 : nums = [1, 2, 3]
출력 : [
        [3],
        [1],
        [2],
        [1, 2, 3],
        [1, 3],
        [2, 3],
        [1, 2],
        []
      ]

Solution 1. 트리의 모든 DFS 결과

입력으로 만들 수 있는 모든 부분집합을 탐색하면 된다.
따라서, DFS로 탐색하며 만들어지는 모든 부분집합을 담아서 반환한다.
'''

import time

def subsets(nums):
    # 결과를 저장할 리스트
    result = []
    
    # dfs 탐색
    def dfs(index, subset):
        # 부분집합 추가
        result.append(subset)

        # 부분집합 탐색 코드
        # 1. 입력(nums)의 index를 순회 
        for i in range(index, len(nums)):
            # 2. 입력의 숫자들로 subset을 구성하고, dfs 재귀 호출
            dfs(i + 1, subset + [nums[i]])

    # 입력(nums)의 0번째 index부터 탐색
    dfs(0, [])
    return result


# 문제에서 주어진 입력
nums = [1, 2, 3]

# 알고리즘 수행 및 수행시간 측정
start_time = time.time() # 시작 시간
result = subsets(nums) # 알고리즘 수행
elapsed_time = time.time() - start_time # 소요된 시간 = 현재 시간 - 시작 시간

# 정답 출력
print(f"Answer : {result}")
# 알고리즘 수행 시간 출력
print(f"Elapsed time : {elapsed_time} [sec]")
