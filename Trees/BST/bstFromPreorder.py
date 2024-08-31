# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def construct_bst_from_preorder(preorder_values):
            if not preorder_values:
                return None
            root = TreeNode(preorder_values[0])
            left_index, right_index = 1, len(preorder_values)

            while left_index < right_index:
                mid = (left_index + right_index) // 2
                if preorder_values[mid] > preorder_values[0]:
                    right_index = mid
                else:
                    left_index = mid + 1
            root.left = construct_bst_from_preorder(preorder_values[1:left_index])
            root.right = construct_bst_from_preorder(preorder_values[left_index:])
            return root
        return construct_bst_from_preorder(preorder)
        
