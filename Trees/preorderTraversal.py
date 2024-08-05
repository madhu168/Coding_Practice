# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self, root: Optional[TreeNode], arr: List[int]) -> None:
        if root is None:
            return
        arr.append(root.val)
        self.preorder(root.left,arr)
        self.preorder(root.right,arr)
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        self.preorder(root,arr)
        return arr