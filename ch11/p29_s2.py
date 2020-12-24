import collections

def numJewelsInStones(J, S):
    freqs = collections.defaultdict(int)
    count = 0

    # 비교 없이 돌(S) 빈도 수 계산
    for char in S:
        freqs[char] += 1

    # 비교 없이 보석(J) 빈도 수 합산
    for char in J:
        count += freqs[char]

    return count

# 입력
J = 'aA'
S = 'aAAbbbb'

# 출력
print(numJewelsInStones(J,S))