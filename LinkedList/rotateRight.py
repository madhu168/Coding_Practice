# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return None
        temp1 = head
        n = 0
        while temp1:
            n += 1
            temp1 = temp1.next
        
        if n == 1:
            return head
        r_k = k % n
        if k == 0 or r_k == 0:
            return head
        slow = head
        fast = head
        for i in range(r_k):
            fast = fast.next
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        

        head2 = slow.next
        slow.next = None
        fast.next = head

        return head2