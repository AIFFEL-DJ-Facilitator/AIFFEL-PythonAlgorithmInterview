'''
19. 역순 연결 리스트 2
인덱스 m에서 n까지를 역순으로 만들어라. 인덱스 m은 1부터 시작한다.

입력 : 1->2->3->4->5->NULL
      m = 2, n = 4

출력 : 1->4->3->2->5->NULL

Solution 1. 반복 구조로 노드 뒤집기
< 책의 238pg 그림 8-9를 같이 보아야 함 >

1.  알고리즘 수행을 위한 기본 설정
    최종 반환을 root.next로 하기 위해, root 노드를 만들어놓는다.
    start는 m-1번째 인덱스, end는 m번째 인덱스(start.next)로 지정한다.

2.  알고리즘 수행
    알고리즘의 핵심은 end가 n번째 노드를 가리킬 때까지 아래의 두 과정을 반복하는 것이다.
    - end의 다음노드를 start의 다음 노드로 옮겨놓기 --> start.next = end.next
    - 위에서 옮겨진 빈 자리를 end가 채우게 하기     --> end.next = end.next.next

    그런데 위의 두가지 작업만 수행하게 된다면, 새롭게 옮겨진 start의 다음 노드가 가리킬 대상에 대한 정보가 없게 된다.
    따라서, 미리 정보를 저장해 놓는 작업이 필요하다. --> tmp = start.next

    위의 전체 과정을 정리하면 다음과 같다.
    1. tmp = start.next         : 새롭게 start.next가 될 노드가 가리킬 대상에 대한 정보 저장
    2. start.next = end.next    : end의 다음노드를 start의 다음 노드로 옮겨놓기
    3. end.next = end.next.next : 위에서 옮겨진 빈 자리를 end가 채우게 하기
    4. start.next.next = tmp    : 새롭게 start.next가 된 노드가 가리킬 대상을 지정해주기
'''

import time


# Linked List의 노드 클래스
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Linked List의 모든 element를 출력하는 함수
def print_all(node):
    while node is not None:
        print(f"{node.val}->", end='')
        node = node.next

    print('NULL')


# 문제에서 구현해야 하는 함수(알고리즘)
def reverse_between(head, m, n):
    # 예외 처리
    if (not head) or (m == n):
        return head

    # 최종 출력은 root.next로 하기 위한 더미노드
    root = ListNode(None)
    root.next = head

    # start가 m-1번째를 노드를 가리키게 함
    start = root
    for _ in range(m - 1):
        start = start.next

    # end가 start의 다음 노드를 가리키게 함
    end = start.next

    # m에서 n까지 노드 뒤집기 수행하는 코드 (상단 주석 참고)
    for _ in range(n - m):
        tmp = start.next # 새롭게 start.next가 될 노드가 가리킬 대상에 대한 정보 저장
        start.next = end.next # end의 다음노드를 start의 다음 노드로 옮겨놓기
        end.next = end.next.next # 위에서 옮겨진 빈 자리를 end가 채우게 하기
        start.next.next = tmp # 새롭게 start.next가 된 노드가 가리킬 대상을 지정해주기

    return root.next


# 문제 풀이에 앞서, 입력 Linked List를 생성
input_head = ListNode(5)
for i in range(4, 0, -1):
    before_node = ListNode(i, input_head)
    input_head = before_node
print_all(input_head)

# 문제에서 주어진 m, n
m, n = 2, 4

# 알고리즘 수행 및 수행시간 측정
start_time = time.time() # 시작 시간
result_head = reverse_between(input_head, m, n)
elapsed_time = time.time() - start_time # 소요된 시간 = 현재 시간 - 시작 시간

# 결과 Linked List가 문제의 출력과 동일한지 확인
print_all(result_head)
# 알고리즘 수행 시간 출력
print(f"Elapsed time : {elapsed_time} [sec]")
