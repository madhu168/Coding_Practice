# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_order(self, root: Optional[TreeNode], m: dict, hd: int, level: int) -> None:
        if root is None:
            return
        if hd not in m:
            m[hd] = []
        m[hd].append([level,root.val])
        self.get_order(root.left,m,hd-1,level+1)
        self.get_order(root.right,m,hd+1,level+1)

    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        m = {}
        hd = 0
        level = 0
        ans = []
        self.get_order(root,m,hd,level)

        for i in sorted(m.keys()):
            m[i].sort()
            l = []
            for level, value in m[i]:
                l.append(value)
            ans.append(l)
        
        return ans