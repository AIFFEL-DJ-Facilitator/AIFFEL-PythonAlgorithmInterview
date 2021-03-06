class ListNode:
    def __init__(self, x=0, next=None):
        self.val = x
        self.next = next

def print_all(node):
    while node is not None:
        print(f"{node.val}->", end='')
        node = node.next

    print('NULL')

def reverseList(head):
    # 재귀 구조
    def reverse(node, prev=None):
        if not node:
            return prev
        next, node.next = node.next, prev
        return reverse(next, node)

    return reverse(head)

# 입력
input_head = ListNode(5)
for i in range(4, 0, -1):
    before_node = ListNode(i, input_head)
    input_head = before_node

# 출력
result_head = reverseList(input_head)
print_all(result_head)

