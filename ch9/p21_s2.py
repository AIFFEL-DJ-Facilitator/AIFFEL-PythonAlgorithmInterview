"""
21. 중복 문자 제거
구체적인 논리에 대해선 풀이 1을 참조해 주세요.
"""

def removeDuplicateLtters(s): # 가장 앞에 나올 알파벳을 찾아 하나씩 stack에 저장하는 알고리즘입니다.
    counter, seen, stack = collections,Counter(s), set(), []

    for char in s:
        count[char] += -1

        if char in seen: # seen은 stack과 문자를 공유합니다. seen에 저장되어있다는 것은 이미 문자열 앞부분(stack)에 기록되었다는 것이므로 더 기록하지 않습니다.
            continue # 기록하지 않고 다음 문자로 넘어갑니다.
        
        while stack and char < stack[-1] and conter[stack[-1]] > 0:
            # 바로 전에 기록된 문자가 뒤에 바꿀 자리가 남아있고(conter[stack[-1]] > 0)
            # 그 문자가 알파벳 순으로 후순위라면 (char < stack[-1])
            seen.remove(stack.pop()) # 제거하고 이를 반복해줍니다. 모든 문자는 stack에 하나씩만 저장되고 seen에도 하나만 저장되기 때문에 한쪽에만 남아있는 경우는 없습니다.
        
        stack.append(char) # 위의 while 문을 통과하면 stack에 추가해줍니다.
        seend.add(char)

    return ''.join(stack)