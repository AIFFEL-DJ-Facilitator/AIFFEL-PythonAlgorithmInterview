import collections

def func(head):
    """
    코드에 대한 구체적인 해설은 1번 풀이를 참조하십시오.
    """
    q = collections.deque() # 데이터를 양방향으로 읽을 수 있는 데크 자료를 형성해줍니다.

    if not head:
        return True
    
    node = head
    while node is not None:
        q.append(node.val)
        node = node.next
    
    while len(q) > 1:
        if q.popleft() != q.pop(): # q의 가장 왼쪽 요소와 마지막 요소를 비교합니다.
            return False
    
    return True