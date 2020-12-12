#sample = 'A man, a plan, a canal: Panama'
#False_sample = 'race a car'
def isPalindrome(s):
    strs = [] #list에 저장하는 방식을 택한다.
    for char in s: 
        if char.isalnum(): #영문자, 숫자 여부를 판별하는 함수 (쉼표, 점은 여기에 해당하지 않는다. [A, ,m,a,n,',', ,a, ,p,l,a,n,',', ,a, ,c,a,n,a,l,:, ,P,a,n,a,m,a]
            strs.append(char.lower()) #소문자로 만들어준다음 append하기[a,m,a,n,a,p,l,a,n,a,c,a,n,a,l,p,a,n,a,m,a]

    while len(strs) > 1:
        if strs.pop(0) != strs.pop(): # 맨 앞에 있는 value와 맨 뒤에 있는 value가 다르면 False로 출력 (pop함수는 지정하면서 list에서 제거된다.) [1. a==a], [2. m==m], [3. a==a]...
            return False #[1. r==r], [2. a==a], [3. c == c], [4. e != a]

    return True