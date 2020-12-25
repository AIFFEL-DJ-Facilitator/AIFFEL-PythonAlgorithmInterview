'''
33. 전화번호 문자 조합

2에서 9까지의 숫자가 주어졌을 때 전화번호로 조합 가능한 모든 문자를 출력하라.
(번호별 알파벳은 책을 참조)

입력 : "23"
출력 : ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

Solution 1. 모든 조합 탐색

아이디어는 간단하다.
단순히 입력에 주어진 번호에 해당하는 알파벳들로 만들 수 있는 모든 조합을 탐색하면 된다.
여기서는 DFS로 문제를 풀이하였다.

- vertex 탐색 방법
입력 숫자를 하나씩 가져오기 위해, index를 for문으로 순회한다. (1)
그리고, 숫자에 해당하는 알파벳을 다시 for문으로 가져온다. (2)
Ex) digits = "23"
    for i in range(0, 1): --> (1)
        for alphabet in range(digits[i]) --> (2)

- vertex 추가하는 시점
입력으로 주어진 숫자의 길이와 알파벳의 길이가 같을 때,
각 숫자에 해당하는 알파벳의 조합이 만들어졌다고 보고 vertex를 추가한다.
Ex) if len("23") == len("a"):
        // vertex 추가 X
    if len("23") == len("ad"):
        // vertex 추가 O


정리하자면, 입력 숫자에 해당하는 알파벳을 for문으로 순회하면서 알파벳 문자 조합을 구성하고,
구성된 문자열의 길이가 입력 숫자의 길이와 같을 때, 추가하는 것이다.
'''

import time

# 문자 조합 출력 함수
def letter_combinations(digits):
    # vertex 추가하는 코드
    def dfs(index, path):
        # 입력 숫자의 길이가 현재 path 길이와 같다면 조합에 추가
        if len(digits) == len(path):
            result.append(path)
            return

        # vertex 탐색하는 코드
        # 1. 입력 숫자의 index를 순회
        for i in range(index, len(digits)):
            # 2. 입력 숫자에 해당하는 알파벳 순회
            for alphabet in dic[digits[i]]:
                # 3. 만들어진 문자 조합으로 dfs 재귀 호출
                dfs(i + 1, path + alphabet)

    # 예외 처리 : digits가 비어있다면 그대로 반환
    if not digits:
        return []

    # 각 숫자에 해당하는 알파벳들
    dic = { "2": "abc", "3": "def", "4": "ghi",
            "5": "jkl", "6": "mno", "7": "pqrs",
            "8": "tuv", "9": "wxyz" }
    result = []

    # 입력 숫자의 0번째 index부터 탐색 시작
    dfs(0, "")

    return result


# 문제에서 주어진 입력
digits = "23"

# 알고리즘 수행 및 수행시간 측정
start_time = time.time() # 시작 시간
result = letter_combinations(digits)
elapsed_time = time.time() - start_time # 소요된 시간 = 현재 시간 - 시작 시간

# 정답 출력
print(f"Answer : {result}")
# 알고리즘 수행 시간 출력
print(f"Elapsed time : {elapsed_time} [sec]")
