# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode()
        current = dummy_node
        carry = 0
        while l1 and l2:
            total = l1.val + l2.val + carry
            if total >= 10:
                carry = 1
                total = total % 10
            else:
                carry = 0
            node = ListNode(total)
            current.next = node
            current = node
            l1 = l1.next
            l2 = l2.next
        
        next_batch = l1 if l1 else l2
        
        while next_batch:
            total1 = next_batch.val + carry
            if total1 >= 10:
                carry = 1
                total1 = total1 % 10
            else:
                carry = 0
            node = ListNode(total1)
            current.next = node
            current = node
            next_batch = next_batch.next
        
        if carry == 1:
            node = ListNode(1)
            current.next = node
        
        return dummy_node.next