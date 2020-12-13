'''
2. 문자열 뒤집기
문자열을 뒤집는 함수를 작성하라.
입력값은 문자 배열이며, 리턴 없이 리스트 내부를 직접 조작하라

입력 : ["h", "e", "l", "l", "o"]
출력 : ["o", "l", "l", "e", "h"]

Solution 1. 투 포인터를 이용한 스왑
- 투 포인터란?
    - 양 끝단을 가리키는 변수를 하나씩(left, right)를 둔 후, 이들을 중앙으로 한칸씩 옮겨가는 방식을 말한다.
      반복문이 끝나는 시점은 left가 right보다 커지는 시점이므로, 주로 left < right를 탈출조건으로 하여 작성하게 된다.
'''
import time

def reverse_string(s):
    # left : 왼쪽 끝이므로, 0
    # right : 오른쪽 끝이므로, (문자열의 길이-1)
    left, right = 0, len(s)-1

    # left가 right보다 작을동안만 반복(커지면 탈출)
    while left < right:
        s[left], s[right] = s[right], s[left] # 문자열의 left번째 원소와 right번째 원소를 바꿈(swap)
        
        left += 1 # left 포인터가 다음 원소를 가리키도록 +1을 해줌
        right -= 1 # right 포인터를 이전 원소를 가리키도록 -1을 해줌


input_str = ["h", "e", "l", "l", "o"]

start_time = time.time() # 시작 시간 측정
reverse_string(input_str) # 문자열 뒤집기 수행
elapsed_time = time.time() - start_time # 소요된 시간 = 현재시간 - 시작 시간

print(input_str) # 뒤집은 결과 출력
print(f"Elapsed time : {elapsed_time} [sec]") # 소요 시간 출력
