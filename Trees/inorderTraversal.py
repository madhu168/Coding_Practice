# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root: Optional[TreeNode], arr: List[int]) -> None:
        if root is None:
            return
        self.inorder(root.left,arr)
        arr.append(root.val)
        self.inorder(root.right,arr)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        self.inorder(root,arr)
        return arr