# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightViewTraversal(self, root: Optional[TreeNode], arr: List[int], level: int) -> None:
        if root is None:
            return
        if level == len(arr):
            arr.append(root.val)
        self.rightViewTraversal(root.right,arr,level+1)
        self.rightViewTraversal(root.left,arr,level+1)
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        self.rightViewTraversal(root,arr,0)
        return arr