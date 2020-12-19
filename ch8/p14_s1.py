#input_sample = 1->2->4, 1->3->4 => l1 = [1,2,4], l2 = [1,3,4]
#output_sample = 1->1->2->3->4->4 => output = [1,1,2,3,4,4]

# Definition for singly-linked list.
 class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeTwoLists(self, l1, l2):
        if (not l1) or(l2 and (l1.val > l2.val)):
            l1, l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1


#l1 = [1,2,4] , l2 = [1,3,4] -> 1 == 1 (첫번째 조건 부합x)
#l1.next = 2,  l2 = [1,3,4] -> 2 > 1 (첫번째 조건 부합) => l1.next = [1,3,4], l2 = 2, l1 = [1,1,3,4,4]
#l1.next.next = 3, l2 = 2 -> 3 > 2 => l1.next.next = 2, l2 = 3, l1.next = [1,2,4], l2 = 3, l1 = [1,1,2,4,4] 
# l1.next.next.next = 4, l2 = 3 -> 4 > 3 => l1.next.next.next = 3, l2 = 4, l1 = [1,1,2,3,4] 
#l1.next.next.next.next.next = None, l2 = 4, l1.next.next.next.next.next = 4, l2 = None, l1 = [1,1,2,3,4,4]