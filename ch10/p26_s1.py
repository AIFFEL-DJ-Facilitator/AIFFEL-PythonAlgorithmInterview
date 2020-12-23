class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#그림으로 설명하는 편이 훨씬 빠르다..

class MyCircularDeque:
    def __init__(self, k):
        self.head, self.tail = ListNode(None), ListNode(None)
        self.k, self.len = k, 0
        self.head.right, self.tail.left = self.tail, self.head

# O(node)-0(n)-O(new)
    def _add(self, node, new):
        n = node.right
        node.right = new
        new.left, new.right = node, n
        n.left = new

# O(node)--0(delete)--O(n)
    def _del(self, node):
        n = node.right.right
        node.right = n
        n.left = node

# 0(head)-ㅁ(value)-0(node1)-O(node2)
    def insertFront(self, value):
        if self.len ==self.k:
            return False
        self.len += 1
        self._add(self.head, ListNode(value))
        return True

# O(node1)-O(node2)-ㅁ(value)-0(tail)
    def insertLast(self, value):
        if self.len == self.k:
            return False
        self.len += 1
        self._add(self.tail.left, ListNode(value))
        return True

# 0(head) - O(node2) 

    def deleteFront(self):
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.head)
        return True

# O(node2) - O(tail)
    def deleteLast(self):
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.tail.left.left)
        return True

# 0(head) - O(value)
    def getFront(self):
        return self.head.right.val if self.len else -1
    
# O(value) - 0(tail)
    def getRear(self):
        return self.tail.left.val if self.len else -1
    
    def isEmpty(self):
        return self.len == 0

    def isFull(self):
        return self.len == self.k
    
