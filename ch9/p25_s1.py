class MyCircularQueue:
    def __init__(self, k):
        self.q = [None] * k # k개의 빈공간 생성
        self.maxlen = k
        self.p1 = 0 # p1(front) 포인터
        self.p2 = 0 # p2(rear) 포인터

    # enQueue : 삽입
    def enQueue(self, value):
        if self.q[self.p2] is None:
            # p2 포인터 가 가르키는 자리에 value 삽입
            self.q[self.p2] = value
            # p2 포인터 한 칸 이동
            # %(나머지) 연산자 사용 이유 : 이동 위치가 큐의 최대길이를 넘어가면 첫 번째 자리에 삽입하기 위해(순서랑 상관X)
            self.p2 = (self.p2 + 1) % self.maxlen 
            return True
        else:
            return False

    # deQueue : 제일 처음 들어온 요소 삭제
    def deQueue(self):
        if self.q[self.p1] is None:
            return False
        else:
            # p1(front) 요소 삭제
            self.q[self.p1] = None
            # p1 포인터 한 칸 이동
            # %(나머지) 연산자 사용하는 이유는 위 enQueue함수와 같음
            self.p1 = (self.p1 + 1) % self.maxlen
            return True
    
    # 제일 처음에 들어온 요소 반환
    def Front(self):
        return -1 if self.q[self.p1] is None else self.q[self.p1]

    # 제일 마지막에 들어온 요소 반환
    def Rear(self):
        return -1 if self.q[self.p2 - 1] is None else self.q[self.p2 - 1]

    # 큐의 빈 공간이 있다면 True
    def isEmpty(self):
        return self.p1 == self.p2 and self.q[self.p1] is None

    # 큐의 빈 공간이 없다면 True
    def isFull(self):
        return self.p1 == self.p2 and self.q[self.p1] is not None

c_queue = MyCircularQueue(5) # [-,-,-,-,-]
print(c_queue.enQueue(10)) # [10,-,-,-,-]
print(c_queue.enQueue(20)) # [10,20,-,-,-]
print(c_queue.enQueue(30)) # [10,20,30,-,-]
print(c_queue.enQueue(40)) # [10,20,30,40,-]
print(c_queue.Rear()) # [10,20,30,40(rear),-]
print(c_queue.isFull()) # [10,20,30,40,-] => 빈 공간 존재하여 False
print(c_queue.deQueue()) # [20,30,40,-,-]
print(c_queue.deQueue()) # [30,40,-,-,-]
print(c_queue.enQueue(50)) # [30,40,50,-,-]
print(c_queue.enQueue(60)) # [30,40,50,60,-]
print(c_queue.Rear()) # [30,40,50,60(rear),-]
print(c_queue.Front()) # [30(front),40,50,60,-]
