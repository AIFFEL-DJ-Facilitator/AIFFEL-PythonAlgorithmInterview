'''
31. 상위 K 빈도 요소

k번 이상 등장하는 요소를 추출하라.(? 번역 오류인 것 같음)
--> 가장 많이 등장하는 요소 k개를 출력하라.

입력 : nums = [1, 1, 1, 2, 2, 3], k = 2
출력 : [1, 2]

Solution 2. 파이썬다운 방식

colllections모듈의 Counter 클래스에 빈도수가 높은 순서대로 출력해주는 함수가 이미 구현되어 있다.
그런데, 이 출력을 살펴보면 다음과 같이 [(priority, element)]의 구조로 반환된다.
[1, 1, 1, 2, 2, 3] --> [(1, 3), (2, 2), (3, 1)]

따라서, 위의 반환 결과에서 element만을 꺼내서 출력해주기 위해 zip과 *를 사용해서 다음과 같이 수행한다.
result = list(zip(*collections.Counter(nums).most_common(k)))[0]

위 코드 한줄의 과정을 풀어서 살펴보면 다음과 같다.

1.  most_common(k)를 통해 k개의 가장 높은 빈도수 요소를 추출한다.(k = 2)
    collections.Counter(nums).most_common(2) --> [(1, 3), (2, 2)]

2.  *를 통해 리스트를 풀어준다.
    [(1, 3), (2, 2)] --> (1, 3), (2, 2)

3.  위 결과를 zip으로 각각의 시퀀스로 바꾼다. (더 정확히는 제너레이터로 반환되는 시퀀스)
    zip((1, 3), (2, 2)) --> 시퀀스 (1) : 1, 2 / 시퀀스 (2) : 3, 2

4.  list로 시퀀스 단위로 묶어준다.
    [시퀀스 (1)] : [1, 2]
    [시퀀스 (2)] : [3, 2]

5. 우리가 원하는 것은 element의 정보이므로, 첫번째 인덱스의 결과를 반환한다.
'''
import time
import collections
import heapq

# 1. Counter 클래스의 most_common() 사용
def top_k_freq_most_common(nums, k):
    return list(zip(*collections.Counter(nums).most_common(k)))[0]


# 문제에서 주어진 nums, k
nums = [1, 1, 1, 2, 2, 3]
k = 2

# 알고리즘 수행 및 수행시간 측정
start_time = time.time() # 시작 시간
answer = top_k_freq_most_common(nums, k)
elapsed_time = time.time() - start_time # 소요된 시간 = 현재 시간 - 시작 시간

# 정답 및 수행시간 출력
print(f"Answer : {answer}")
print(f"Elapsed time : {elapsed_time} [sec]")

