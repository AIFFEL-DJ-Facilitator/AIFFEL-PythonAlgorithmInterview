import collections
import re
from typing import List

def mostCommonWord(paragraph, banned):
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
        .lower().split()
                if word not in banned]
    # re.sub()
    # replace()함수와 비슷하고 패턴이 있는 문자열 치환에 유리
    # re.sub('패턴', '교체할 문자열', '입력 문자열', '교체 단어 개수')

    # 문자 외 공백으로 치환(sub), 소문자 변환(lower), 단어를 요소로 리스트로 변환(split)
    # if문에서 banned 단어를 제외함

    # 아래 print문의 주석을 풀면 리스트 words를 출력하여 요소를 확인할 수 있음
    # print(words)

    counts = collections.Counter(words)
    # Counter() : 리스트의 요소들을 개수를 셈

    # 아래 print문의 주석을 풀면 counts가 딕셔너리 형태로 '단어':빈도 수 쌍인 것을 볼 수 있음
    # print(counts)

    return counts.most_common(1)[0][0]
    # most_common(n) : 가장 많이 나타난 n개를 출력
    # ex) n이 2이면 가장 많이 나타나는 2개의 단어 출력 

# 입력
paragraph = 'Bob hit a ball, the hit BALL flew far after it was hit.'
banned = ["hit"]


# 출력
print(mostCommonWord(paragraph,banned))