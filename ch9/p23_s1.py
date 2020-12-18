'''
23. 큐를 이용한 스택 구현
큐를 이용해 다음 연산을 지원하는 스택을 구현하라.
- push(x) : 요소 x를 스택에 삽입한다.
- pop() : 스택의 첫번째 요소를 삭제 및 반환한다.
- top() : 스택의 첫번째 요소를 반환한다.
- empty() : 스택이 비어 있는지 여부를 반환한다.

Solution 1. push() 할 때 큐를 이용해 재정렬
collections의 deque 라이브러리를 통해 쉽게 구현이 가능하다.
push를 통해 원소가 들어올 때마다 역순으로 재정렬해주면 된다.
'''
from collections import deque


class MyStack:
    def __init__(self):
        self.stack = deque()

    def push(self, item):
        self.stack.append(item)
        # 역순으로 재정렬
        for _ in range(len(self.stack) - 1):
            self.stack.append(self.stack.popleft())
            
    def top(self):
        # stack이 빈 경우, None을 출력
        if len(self.stack) == 0:
            return None

        return self.stack[0]

    def pop(self):
        # stack이 빈 경우, None을 출력
        if len(self.stack) == 0:
            return None

        return self.stack.popleft()

    def empty(self):
        return len(self.stack) == 0
    

stack = MyStack()
stack.push(1)
stack.push(2)
print(f"stack.top() : {stack.top()}")
print(f"stack.pop() : {stack.pop()}")
print(f"stack.empty() : {stack.empty()}")