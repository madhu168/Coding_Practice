# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None



# clone the given node as it's next node and delete the next node

class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next

        