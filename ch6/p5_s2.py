#set의 성질을 이용한 커스텀 풀이입니다.

strs = ["eat","tea","tan","ate","nat","bat"]

def sub_func(strs, total): # set은 중복을 허용하지 않는다는 것을 이용한 풀이 방식입니다.
  a = None
  a_list = []
  for st in strs:
    if a is not None: # 기준이 되는 a가 이미 생성되었다는 의미입니다.
      if set(st) == a: # set으로 만들었을때 기준이 되는 a와 같은 알파벳으로 이루어져있으면 같은 anagram으로 확인합니다.
        a_list.append(st) # 같은 anagram이므로 하나로 묶어줍니다.
    else:
      a = set(st) # a에 등록된 set 값이 없을때 필터가 될 set 값을 설정해줍니다.
      a_list.append(st)
  total.append(a_list)
  for temp in a_list:
    strs.remove(temp) # a_list에 포함된 요소들이 중복되어 사용되지 않도록 제거합니다.
  return strs, total # return 선언을 통해 함수 밖의 strs와 total을 업데이트 해줍니다.

def main_func(strs):
  total = []
  while len(strs) > 0: # strs의 모든 요소가 각각 구분되어 total에 모두 포함되면 strs의 길이는 0이 됩니다.
    sub_func(strs, total)
  return total

print(main_func(strs))
