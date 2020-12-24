def numJewelsInStones(J, S):
    freqs = {}
    count = 0

    # 돌(S)의 빈도 수 계산
    for char in S:
        if char not in freqs:
            freqs[char] = 1
        else:
            freqs[char] += 1

    # 보석(J)의 빈도 수 합산
    for char in J:
        if char in freqs:
            count += freqs[char]

    return count

# 입력
J = 'aA'
S = 'aAAbbbb'

# 출력
print(numJewelsInStones(J,S))