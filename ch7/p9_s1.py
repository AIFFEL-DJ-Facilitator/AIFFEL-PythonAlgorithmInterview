'''
9. 세 수의 합
배열을 입력받아 합으로 0을 만들 수 있는 3개의 element를 출력하라.

입력 : nums = [-1, 0, 1, 2, -1, -4]
출력 : [(-1, -1, 2), (-1, 0, 1)]

Solution 1. 브루트 포스로 계산
먼저, 입력(nums)에 동일한 값의 element(이 문제에서는 -1)가 있는 경우를 처리하기 위해 sort()를 통해 정렬을 수행한다.
그리고, i, j, k로 0을 만들 수 있는 모든 조합의 인덱스를 탐색한다.
'''

import time


def three_sum(nums):
    results = [] # 결과(0이 되는 3개의 element 조합들)를 저장할 리스트
    nums.sort() # 입력(nums) 데이터를 오름차순으로 정렬

    # 3개의 포인터(i, j, k)를 움직이며 모든 조합을 탐색
    for i in range(len(nums) - 2): # i 범위 탐색
        # 바로 이전의 값과 현재의 값이 같다면(중복인 경우) skip
        # 이때, i > 0을 검사하는 이유는 첫번째 루프에는 이전의 수행한 비교할 값이 없기 때문
        if i > 0 and (nums[i] == nums[i - 1]):
            continue
            
        for j in range(i + 1, len(nums) - 1): # j 범위 탐색
            # 바로 이전의 값과 현재의 값이 같다면(중복인 경우) skip
            # 이때, j > i + 1을 검사하는 이유는 첫번째 루프에는 이전의 수행한 비교할 값이 없기 때문
            if j > i + 1 and (nums[j] == nums[j - 1]):
                continue

            for k in range(j + 1, len(nums)): # k 범위 탐색
                # 바로 이전의 값과 현재의 값이 같다면(중복인 경우) skip
                # 이때, k > j + 1을 검사하는 이유는 첫번째 루프에는 이전의 수행한 비교할 값이 없기 때문
                if k > j + 1 and nums[k] == nums[k - 1]:
                    continue
                
                # 0이 나오는 조합을 찾으면, results에 저장
                if nums[i] + nums[j] + nums[k] == 0:
                    results.append((nums[i], nums[j], nums[k]))

    # 결과 반환
    return results


nums = [-1, 0, 1, 2, -1, -4]

start_time = time.time() # 시작 시간 측정
result = three_sum(nums) # 결과 출력
elapsed_time = time.time() - start_time # 소요된 시간 = 현재시간 - 시작 시간

print(result) # 결과 출력
print(f"Elapsed time : {elapsed_time} [sec]") # 소요 시간 출력
