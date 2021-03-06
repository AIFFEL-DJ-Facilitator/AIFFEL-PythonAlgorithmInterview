strs = ["eat","tea","tan","ate","nat","bat"]

import collections
# sample_data = ['bat', 'tab']

def func(strs):
  anagrams = collections.defaultdict(list) # 딕셔너리의 value를 list 데이터로 저장합니다.
  """
  collections 모듈은 많은 기능을 갖고 있습니다. 숫자를 세고 기본적인 통계(최대, 최소, 평균 등)를 할 수 있는 count함수,
  양방향 데이터 처리가 요구되는 queue형 자료처리를 위한 deque 함수,
  그리고 dictionary 관리를 위한 defaultdict함수 등이 있죠.
  defaultdict 함수는 새로운 키가 등록될때 에러없이 default 값의 형태로 받을 수 있습니다.
  collections.defaultdict({list, int, str...등}, key1 = value1, key2 = value2...)
  https://excelsior-cjh.tistory.com/95를 참조하면 더 구체적인 정보를 얻을 수 있습니다.
  """
  for word in strs:
    anagrams[''.join(sorted(word))].append(word)
    # sorted 함수는 각 단어를 글자별로 분리한 후 정렬해서 리스트로 반환합니다. ['a', 'b', 't']
    # 정렬된 리스트를 join 함수를 통해 다시 문자열로 합치고 이를 dictionary의 key로 입력합니다. 'abt'
    # 위에서 입력한 키에 원래 문자열을 value로 하여 입력합니다.
    # 최종 결과는 다음과 같습니다. anagram = {'abt' : ['bat', 'tab']}
  return anagrams.values()

print(func(strs))
