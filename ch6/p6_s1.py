def longestPalindrome(s):
    # 팰린드롬 판별 및 투 포인터 확장
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    if len(s) < 2 or s == s[::-1]: # 입력 문자열이 길이가 2보다 작거나 
                                   # 거꾸로 나열했을 때 입력 문자열과 같으면
                                   # 입력 문자열 자체가 팰린드롬 
        return s

    result = ''
    # 슬라이딩 윈도우 우측으로 이동
    for i in range(len(s) - 1):
        result = max(result,
                        expand(i, i + 1), # 팰린드롬 길이가 짝수
                        expand(i, i + 2), # 팬린드롬 길이가 홀수
                        key=len) # key=len을 lambda n:len(n)로 생각하면 됨
        print(result)
    return result

# 입력
s1 = 'babad'
# s2 = 'cbbd'

# 출력
print(longestPalindrome(s1))
# print(longestPalindrome(s2))