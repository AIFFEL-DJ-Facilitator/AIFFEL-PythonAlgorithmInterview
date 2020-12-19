#T = [73, 74, 75, 71, 69, 72, 76, 73]
#output = [1,1,4,2,1,1,0,0]

def solution(T):
    answer = [0] * len(T) #answer = [0,0,0,0,0,0,0,0]
    stack = []

    for i, cur in enumerate(T): # i=[0,1,2,3,4,5,6,7,8], cur = [73,74,75,71,69, 72, 76, 73]
        while stack and cur > T[stack[-1]]: # 74 > 73
            last = stack.pop() # stack = [], last = 0
            ansewr[last] = i - last #answer = [1-0, 0,0,0,0,0,0,0,0] 

        stack.append(i) # stack = [0] -> stack = [1]

    return answer

