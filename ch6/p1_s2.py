#sample = 'A man, a plan, a canal: Panama'
#False_sample = 'race a car'
import collections

def isPalindrome(s):
    strs = collections.deque() # double_ended_queue의 줄임말로 양방향으로 처리할 수 있는 queue형 자료구조이다. python에서 list와 매우 유사하며 특정 메서드가 있는데 이 분제에서는 popleft를 이용하기 위해서 사용했다.

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop(): # deque에서는 popleft라는 매서드를 사용할 수 있다.
            return False

    return True