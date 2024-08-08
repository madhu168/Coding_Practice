# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self,root: Optional[TreeNode], d: List[int]) -> int:
        if root is None:
            return 0
        left = self.traverse(root.left,d)
        right = self.traverse(root.right,d)
        d[0] = max(d[0],left+right)
        return 1 + max(left,right)
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d = [0]
        self.traverse(root,d)
        return d[0]