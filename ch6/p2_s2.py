'''
2. 문자열 뒤집기
문자열을 뒤집는 함수를 작성하라.
입력값은 문자 배열이며, 리턴 없이 리스트 내부를 직접 조작하라

입력 : ["h", "e", "l", "l", "o"]
출력 : ["o", "l", "l", "e", "h"]

Solution 2. 파이썬 다운 방식
- 파이썬의 기본 기능을 활용하면 된다.(이런 것을 Pythonic하다라고 함)
- list의 내장함수인 reverse()를 사용하거나 슬라이싱을 통해 수행할 수 있다.(두방법 모두 가능)
  주의할 것은 슬라이싱을 사용할 때, s = s[::-1]는 내부 원소에 직접 접근해서 값을 변경해주는 것이 아니기 때문에 동작하지 않는다는 것이다.
  따라서, s[:] = s[::-1]로 작성해야 한다.
'''
import time

def reverse_string(s):
    # 1. 내장함수 reverse()를 사용하는 방법
    s = s.reverse()
    # 2. 슬라이싱을 사용하는 방법
    # s[:] = s[::-1]


input_str = ["h", "e", "l", "l", "o"]

start_time = time.time() # 시작 시간 측정
reverse_string(input_str) # 문자열 뒤집기 수행
elapsed_time = time.time() - start_time # 소요된 시간 = 현재시간 - 시작 시간

print(input_str) # 뒤집은 결과 출력
print(f"Elapsed time : {elapsed_time} [sec]") # 소요 시간 출력
