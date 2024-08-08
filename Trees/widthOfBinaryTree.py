# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, m: dict, root: Optional[TreeNode], hd: int, level: int) -> None:
        if root is None:
            return
        if level not in m:
            m[level] = []
        m[level].append(hd)
        self.traverse(m,root.left,hd*2,level+1)
        self.traverse(m,root.right,hd*2+1,level+1)

    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        m = {}
        hd = 0
        level = 0
        self.traverse(m,root,hd,level)
        max_width = 0
        for key in sorted(m.keys()):
            if len(m[key]) > 1:
                m[key].sort()
                max_width = max(max_width,m[key][-1]-m[key][0]+1)
            elif len(m[key]) == 1:
                max_width = max(max_width, 1)
        return max_width