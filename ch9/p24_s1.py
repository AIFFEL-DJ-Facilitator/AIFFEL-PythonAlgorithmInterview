'''
24. 스택을 이용한 큐 구현
스택을 이용해 다음 연산을 지원하는 큐를 구현하라.
- push(x) : 요소 x를 큐 마지막에 삽입한다.
- pop() : 큐 처음에 있는 요소를 제거한다.
- peek() : 큐 처음에 있는 요소를 반환한다.
- empty() : 큐가 비어 있는지 여부를 반환한다.

Solution 1. 스택 2개 사용
이 방법은 stack을 2개를 사용한다. 설명을 위해 스택 input과 output가 있다고 하자.

push(x)를 통해 데이터가 들어올 때에는 스택 input에 데이터를 쌓는다.
pop()이나 peek()를 호출할 시에는 다음의 2단계로 수행한다.
    1. 스택 input에 있는 데이터를 모두 스택 output에 넣는다.
       (이 과정을 통해 스택 output에는 스택 input의 데이터들이 역순으로 쌓이게 된다.)
       (코드에서는 output이 비어있을 때, 이 과정을 수행하도록 구현하였음)
    2. 스택 output에서 꺼내서 출력한다.
'''


class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []


    def push(self, item):
        self.input.append(item)

            
    def pop(self):
        # 데이터 반환을 위해 peek()를 호출해서 output에 input 데이터를 옮긴다.
        self.peek()
        # output 스택의 마지막 원소를 반환 후 제거한다.
        return self.output.pop()


    def peek(self):    
        # output이 비어있으면 input의 모든 원소를 output에 저장
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())

        # output 스택의 마지막 원소를 반환한다.(뒤집혀있으므로, 마지막 원소가 제일 첫 원소가 됨)
        return self.output[-1]


    def empty(self):
        # 두 스택이 모두 비어있는지 여부를 반환한다.
        return self.input == [] and self.output == []
    

queue = MyQueue()

queue.push(1)
queue.push(2)

print(f"queue.peek() : {queue.peek()}")
print(f"queue.pop() : {queue.pop()}")
print(f"queue.empty() : {queue.empty()}")