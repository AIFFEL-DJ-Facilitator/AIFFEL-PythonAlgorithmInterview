import collections

def numJewelsInStones(J, S):
    # collections의 Counter함수 Reference
    # https://excelsior-cjh.tistory.com/94
    freqs = collections.Counter(S)
    '''
    Counter({'b': 4, 'A': 2, 'a': 1})
    '''
    count = 0
    
    for char in J:
        count += freqs[char]

    return count

# 입력
J = 'aA'
S = 'aAAbbbb'

# 출력
print(numJewelsInStones(J,S))