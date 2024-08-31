# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        def dfs(root) -> tuple:
            if root is None:
                return True, float('inf'),float('-inf'),0
            
            left_is_bst, left_min, left_max, left_sum = dfs(root.left)
            right_is_bst,right_min,right_max, right_sum = dfs(root.right)

            if left_is_bst and right_is_bst and left_max < root.val < right_min:
                subtree_sum = left_sum + right_sum + root.val
                nonlocal max_sum
                max_sum = max(max_sum,subtree_sum)
                return True, min(left_min,root.val),max(right_max,root.val),subtree_sum
            
            return False,0,0,0
        max_sum = 0
        dfs(root)
        return max_sum