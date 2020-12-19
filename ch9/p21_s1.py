"""
21. 중복 문자 제거

사전식 순서로 나열할것.
'bcabc' -> 'abc'
중복을 제거함으로서 만들 수 있는 모든 순열 중 사전식으로 나열했을때 첫번째를 만들어라. 아래와 같이 한번 만들어보면 이해가 될겁니다.

간단하게 사전식 순서로 만드는 방법

1. 중복 없는 글자들은 움직이지 않습니다.
2. 중복 글자들은 기존의 자기 자리 중 하나를 고를 수 있습니다.
3. 가능한 알파벳 순을 맞춰줍니다.

ccfaabeed 라면, b, d, f가 유일하기 때문에
bdf는 고정(아래 설명에선 대문자로 표기),
a, c, e는 조합할 여지가 있기 때문에 각각의 위치 중 하나를 골라 cFaBeD가 됩니다.

(S = 여러개의 c, e, a로 이루어진 랜덤 문자)

주어진 문자는 S + F + S + B + S + D + S 라고 하죠.
그럼 결과는 a, c, e 모두 f보다 작기 때문에 가장 앞에 알파벳 순으로 정렬됩니다.

aceFBD

f와 d의 자리를 바꾸면 결과는 확실히 보일 것입니다.

S + D + S + B + S + F + S

a, c는 d보다 앞이기 때문에 여전히 가장 앞에 알파벳 순으로 정렬되지만 e의 경우 d의 뒤쪽으로 밀립니다.
여기에서 다음에 오는 b보다 순서에 밀리고 f보다 앞이기 때문에 acDBeF 가 됩니다.
여기서 만일 b를 k로 바꾼다면 e는 k보다 알파벳 순이 높으니까 k 앞에 위치할 수 있습니다.

acDeKF
"""

S = 'ceace' + 'f' + 'aceaeceac' + 'b' + 'eaccaec' + 'd' + 'aaeecc'

def smallestSubsequence(S):
    last = {c: i for i, c in enumerate(S)}
    stack = []
    for i, c in enumerate(S):
        if c in stack: continue
        while stack and stack[-1] > c and i < last[stack[-1]]:
            stack.pop()
        stack.append(c)
    return "".join(stack)

S = 'ceace' + 'f' + 'aceaeceac' + 'b' + 'eaccaec' + 'd' + 'aaeecc'
print(smallestSubsequence(S))
print('aceFBD')

S = 'ceace' + 'd' + 'aceaeceac' + 'b' + 'eaccaec' + 'f' + 'aaeecc'
print(smallestSubsequence(S))
print('acDBeF')

S = 'ceace' + 'd' + 'aceaeceac' + 'k' + 'eaccaec' + 'f' + 'aaeecc'
print(smallestSubsequence(S))
print('acDeKF')

"""
주의! 첫번째 S는 완전 랜덤이 아니게 되었습니다.
이 경우 a는 여전히 d 앞에 올 수 있지만 c, e가 다른 자리가 있음에도 a 앞에 오는건 사전식 순서가 아닙니다.
때문에 b와 f 사이에 들어가게 됩니다. 만일 d와 b의 위치를 바꾼다면 어떻게 될까요? 
"""
S = 'cea' + 'd' + 'aceaeceac' + 'b' + 'eaccaec' + 'f' + 'aaeecc'
print(smallestSubsequence(S))
print('aDBceF')

"""
c는 d 앞에 올 수 있기 때문에 aBcDeF가 됩니다.
"""
S = 'cea' + 'b' + 'aceaeceac' + 'd' + 'eaccaec' + 'f' + 'aaeecc'
print(smallestSubsequence(S))
print('aBcDeF')

def removeDuplicateLtters(s): # 가장 앞에 나올 알파벳만을 찾는 알고리즘입니다. 이것을 반복하며 다음 순서 알파벳을 찾습니다.
    for char in sorted(set(s)): #[a,b,c,d,e,f]
        suffix = s[s.index(char):] # char가 a라면 본래 입력 문자열에서 처음 나오는 a부터 끝까지를 suffix라고 합니다. 
        if set(s) == set(suffix): # suffix의 set이 본래 문자열의 set과 같다면 해당 글자는 가장 앞에 오는 글자입니다.
            return char + self.removeDuplicateLtters(suffix.replace(char, '')) # 해당 글자를 제거하고 남은 것에서 반복합니다.
    return ''

"""본래 문자열이 bcbdaef라고 할 때 set(s) = [a, b, c, d, e, f]입니다.

이를 하나씩 돌려보면,

char = a면 suffix = aef고 set(suffix) = abe지만 set(s)는 abcdef기 때문에 다음 문자열로 넘어갑니다.

char = b면 suffix = bcdaef고 set(suffix) = abcdef, set도 abcdef이므로 b가 골라집니다.

이후 전체 문자열에서 방금 고른 b를 제거한 cdaef를 다시 함수로 돌려 시행하게 됩니다.
"""

