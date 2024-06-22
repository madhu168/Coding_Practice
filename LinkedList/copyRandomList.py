"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        # create new duplicate nodes    
        current = head
        while current:
            cloned_node = Node(current.val,current.next)
            current.next = cloned_node
            current = cloned_node.next
        
        current = head
        # add random pointer nodes 
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next
        
        original_current_head = head
        cloned_head = head.next

        # seperate the created nodes from original nodes 
        while original_current_head:
            cloned_current = original_current_head.next
            original_current_head.next = cloned_current.next
            if cloned_current.next:
               cloned_current.next = cloned_current.next.next
            original_current_head = original_current_head.next
        
        return cloned_head


        