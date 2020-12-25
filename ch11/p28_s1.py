import collections

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyHashMap:
    def __init__(self):
        self.size = 1000 # 임의로 정함
        self.table = collections.defaultdict(ListNode)

    def put(self, key, value):
        index = key % self.size # h(x) = x mod m
        if self.table[index].value is None: # 해쉬 충돌이 없을 때 
            self.table[index] = ListNode(key, value)
            return
        p = self.table[index]
        while p: 
            if p.key == key: # 키가 (윤아 30 -> 윤아 15)
                p.value = value
                return

            if p.next is None: # 끝까지 움직인 경우 
                break
            p = p.next 
        p.next = ListNode(key, value) # (윤아 15 - 서현 17)

    def get(self, key):
        index = key % self.size
        if self.table[index].value is None:
            return -1
        
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    def remove(self, key):
        index = key % self.size
        if self.table[index].value is None:
            return

        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next