# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_pointer = ListNode()
        dummy_pointer.next = head
        slow_pointer = fast_pointer = dummy_pointer
        for i in range(n):
            fast_pointer = fast_pointer.next
        
        while fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next
        
        slow_pointer.next = slow_pointer.next.next
        return dummy_pointer.next
