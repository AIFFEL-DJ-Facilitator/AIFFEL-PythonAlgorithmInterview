# sample = 'A man, a plan, a canal: Panama'
# False_sample = 'race a car'

import re # 정규표현식에 관련한 내용이다. (커리큘럼상에서 fundamental 노드에서 만날 수 있다. 이해가 되지 않은 학생들이 많다면 fundamental 노드를 보는 것도 추천)

def isPalindrome(s):
    s = s.lower() # a man, a plan, a canal: panama
    s = re.sub('[^a-z0-9]', '', s) # amanaplanacanalpanama

    return s ==s[::-1] #(False sample)[raceacar != racaecar]