'''
31. 상위 K 빈도 요소

k번 이상 등장하는 요소를 추출하라.(? 번역 오류인 것 같음)
--> 가장 많이 등장하는 요소 k개를 출력하라.

입력 : nums = [1, 1, 1, 2, 2, 3], k = 2
출력 : [1, 2]

Solution 1. Counter를 이용한 음수 순 추출

기본적인 아이디어는 다음과 같다.
1.  입력 데이터의 각 요소별로 몇개씩이 있는지를 헤아린다.
2.  다음과 같이 갯수를 priority, 값을 해당하는 요소의 구조로 만들어서 max heap으로 정렬한다.
    [1, 1, 1, 2, 2, 3] --> [(3, 1), (2, 2), (1, 3)]

그런데 파이썬의 heapq 모듈은 최소 힙만을 지원하기 때문에, 아래와 같이 priority에 음의 값을 취해서 저장하면 된다.
[1, 1, 1, 2, 2, 3] --> [(-3, 1), (-2, 2), (-1, 3)]

그리고, 위와 같이 만들어진 heap에서 총 k번 element를 출력한다.
'''

import time
import collections
import heapq


def top_k_frequent(nums, k):
    # Counter 객체를 이용해 {element : freq}의 형태로 구성한다.
    freqs_dict = collections.Counter(nums)

    # heapq에 [(-3, 1), (-2, 2), (-1, 3)]의 형태로 push한다.
    freqs_heap = []
    for i in freqs_dict:
        heapq.heappush(freqs_heap, (-freqs_dict[i], i))
    
    # k개의 상위 요소(정답)를 담을 list()
    topk = []
    
    # k번 반복해서 heapq에서 상위 요소를 꺼낸다.
    for _ in range(k):
        # 반환 값은 (prior, elem)이므로, 1번째 index 값을 정답 리스트에 담는다.
        topk.append(heapq.heappop(freqs_heap)[1])

    return topk


# 문제에서 주어진 nums, k
nums = [1, 1, 1, 2, 2, 3]
k = 2

# 알고리즘 수행 및 수행시간 측정
start_time = time.time() # 시작 시간
answer = top_k_frequent(nums, k)
elapsed_time = time.time() - start_time # 소요된 시간 = 현재 시간 - 시작 시간

# 정답 출력
print(f"Answer : {answer}")
# 알고리즘 수행 시간 출력
print(f"Elapsed time : {elapsed_time} [sec]")
