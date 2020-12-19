# 연결리스트 생성 class
class ListNode:
    def __init__(self, x=0, next=None):
        self.val = x
        self.next = next

# 출력함수
def print_all(node):
    while node is not None:
        print(f"{node.val}->", end='')
        node = node.next
    print('NULL')

def oddEvenList(head):
    # 예외 처리
    if head is None:
        return None

    odd = head
    even = head.next
    even_head = head.next

    # 반복하면서 홀짝 노드 처리
    while even and even.next:
        # 2칸 이동해야 홀수는 다시 홀수, 짝수는 다시 짝수
        odd.next, even.next = odd.next.next, even.next.next
        odd, even = odd.next, even.next

    # 홀수 노드의 마지막을 짝수 헤드로 연결
    odd.next = even_head
    return head

# 입력
input_head = ListNode(5)
for i in range(4, 0, -1):
    before_node = ListNode(i, input_head)
    input_head = before_node

# 출력
result_head = oddEvenList(input_head)
print_all(result_head)