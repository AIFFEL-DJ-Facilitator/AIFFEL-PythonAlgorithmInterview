'''
9. 세 수의 합
배열을 입력받아 합으로 0을 만들 수 있는 3개의 element를 출력하라.

입력 : nums = [-1, 0, 1, 2, -1, -4]
출력 : [(-1, -1, 2), (-1, 0, 1)]

Solution 2. 투 포인터로 합 계산
먼저, 입력(nums)에 동일한 값의 element(이 문제에서는 -1)가 있는 경우를 처리하기 위해 sort()를 통해 정렬을 수행한다.
그리고, i를 0부터 증가시키면서 진행하는데,
i번째 원소를 제외한 나머지 원소들의 왼쪽과 오른쪽 끝을 left, right라는 두개의 포인터로 두고
이 두 포인터가 중앙으로 모이면서 조합을 탐색하는 방식이다. (교재의 186pg 그림 7-8 참고)
'''

import time


def three_sum(nums):
    results = [] # 결과(0이 되는 3개의 element 조합들)를 저장할 리스트
    nums.sort() # 입력(nums) 데이터를 오름차순으로 정렬

    # i를 0부터 증가시키면서 탐색 진행
    for i in range(len(nums) - 2):
        # 바로 이전의 값과 현재의 값이 같다면(중복인 경우) skip
        # 이때, i > 0을 검사하는 이유는 첫번째 루프에는 이전의 수행한 비교할 값이 없기 때문
        if i > 0 and nums[i - 1] == nums[i]:
            continue

        left = i + 1 # i 바로 다음 원소
        right = len(nums) - 1 # 맨 끝 원소

        # i번째 원소를 제외한 나머지 원소들을 탐색(left 포인터가 right 포인터를 넘어설 때까지)
        while left < right:
            s = nums[i] + nums[left] + nums[right] # 세 원소의 합 계산

            if s < 0:
                # s가 0보다 작다면 값이 커져야 하므로, left 포인터를 + 1
                left += 1
            elif s > 0:
                # s가 0보다 크다면 값이 작아져야 하므로, right 포인터에 - 1
                right -= 1
            else:
                # s가 0이라면, 정답을 찾은 경우이므로 results에 저장 
                results.append((nums[i], nums[left], nums[right]))

                # 다음 left나 right에 동일한 값이 있을 수 있으므로, 이들을 검사하며 skip
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                # 다시 다음 원소들을 탐색
                left += 1 
                right -= 1

    return results


nums = [-1, 0, 1, 2, -1, -4]

start_time = time.time() # 시작 시간 측정
result = three_sum(nums) # 결과 출력
elapsed_time = time.time() - start_time # 소요된 시간 = 현재시간 - 시작 시간

print(result) # 뒤집은 결과 출력
print(f"Elapsed time : {elapsed_time} [sec]") # 소요 시간 출력
