def numJewelsInStones(J, S):
    freqs = {}
    count = 0

    for char in S:
        if char not in freqs:
            freqs[char] = 1
        else:
            freqs[char] += 1
    '''
    문자열 S를 {문자 단위 : 개수}로 딕셔너리
    {'a': 1}
    {'a': 1, 'A': 1}
    {'a': 1, 'A': 2}
    {'a': 1, 'A': 2, 'b': 1}
    {'a': 1, 'A': 2, 'b': 2}
    {'a': 1, 'A': 2, 'b': 3}
    {'a': 1, 'A': 2, 'b': 4}
    '''

    for char in J:                  # 문자열 J의 문자 단위마다 char에 대입하고
        if char in freqs:           # freqs 딕셔너리 key 중 char가 존재한다면 / 없어도 됨
            count += freqs[char]    # char의 value를 더함

    return count

# 입력
J = 'aA'
S = 'aAAbbbb'

# 출력
print(numJewelsInStones(J,S))