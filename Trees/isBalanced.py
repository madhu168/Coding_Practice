# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self,root: Optional[TreeNode]) -> bool:
        if root is None:
            return 0
        left = self.check(root.left)
        right = self.check(root.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return 1 + max(left,right)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.check(root) != -1