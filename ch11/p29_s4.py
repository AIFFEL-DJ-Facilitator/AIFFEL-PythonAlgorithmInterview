def numJewelsInStones(J, S):
    return sum(s in J for s in S)

# 입력
J = 'aA'
S = 'aAAbbbb'

# 출력
print(numJewelsInStones(J,S))