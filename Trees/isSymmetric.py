# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isMirror(self, node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None or node1.val != node2.val:
            return False
        return self.isMirror(node1.left,node2.right) and self.isMirror(node1.right,node2.left)
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isMirror(root,root)