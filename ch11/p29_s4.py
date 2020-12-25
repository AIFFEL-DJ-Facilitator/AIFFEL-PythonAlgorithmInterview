def numJewelsInStones(J, S):
    # print([s for s in S])
    '''
    ['a', 'A', 'A', 'b', 'b', 'b', 'b']
    '''

    # print([s in J for s in S])
    '''
    [True, True, True, False, False, False, False]
    '''
    return sum(s in J for s in S) # True 개수를 더함

# 입력
J = 'aA'
S = 'aAAbbbb'

# 출력
print(numJewelsInStones(J,S))