class Solution:
    def findPreSuc(self, root, pre, suc, key):
        # Your code goes here
        if root is None:
            return
        if root.key == key:
            if root.left is not None:
                tmp = root.left
                while tmp.right:
                    tmp = tmp.right
                pre = tmp
            
            if root.right is not None:
                tmp = root.right
                while tmp.left:
                    tmp = tmp.left
                suc = tmp
            return
        elif root.key > key:
            suc = root
            self.findPreSuc(root.left,pre,suc,key)
        else:
            pre = root
            self.findPreSuc(root.right,pre,suc,key)