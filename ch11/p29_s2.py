import collections

def numJewelsInStones(J, S):
    # collections의 defaultdict함수 Reference
    # https://www.daleseo.com/python-collections-defaultdict/
    freqs = collections.defaultdict(int)
    count = 0

    for char in S:
        freqs[char] += 1
    '''
    문자열 S를 {문자 단위 : 개수}로 딕셔너리
    defaultdict(<class 'int'>, {'a': 1})
    defaultdict(<class 'int'>, {'a': 1, 'A': 1})
    defaultdict(<class 'int'>, {'a': 1, 'A': 2})
    defaultdict(<class 'int'>, {'a': 1, 'A': 2, 'b': 1})
    defaultdict(<class 'int'>, {'a': 1, 'A': 2, 'b': 2})
    defaultdict(<class 'int'>, {'a': 1, 'A': 2, 'b': 3})
    defaultdict(<class 'int'>, {'a': 1, 'A': 2, 'b': 4})
    '''

    for char in J:              # 문자열 J의 문자 단위마다 char에 대입하고
        count += freqs[char]    # freqs 딕셔너리 char의 value를 더함

    return count

# 입력
J = 'aA'
S = 'aAAbbbb'

# 출력
print(numJewelsInStones(J,S))