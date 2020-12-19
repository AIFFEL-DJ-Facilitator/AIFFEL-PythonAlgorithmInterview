 # input_sample = [1,2,3,4]
 # output_sample = [2,1,4,3]
 class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def solution1(self, input):
        cur = input

        while cur and cur.next:
            cur.val, cur.next.val = cur.next.val, cur.val #[1,2] = [2,1]
            cur = cur.next.next # cur = 3 -> [3,4] = [4,3]

        return input #[2,1,4,3]