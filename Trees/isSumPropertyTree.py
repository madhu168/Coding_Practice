# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    #Function to check whether all nodes of a tree have the value 
    #equal to the sum of their child nodes.
    def isSumProperty(self, root):
        # code here
        left_data = 0
        right_data = 0
        
        if((root is None) or (root.left == None and root.right == None)):
            return 1
        else:
            if root.left:
                left_data = root.left.data
            
            if root.right:
                right_data = root.right.data
                
            if ((root.data == (left_data + right_data)) and self.isSumProperty(root.left) and self.isSumProperty(root.right)):
                return 1
            else:
                return 0