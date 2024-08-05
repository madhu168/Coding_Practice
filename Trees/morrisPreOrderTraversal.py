from os import *
from sys import *
from collections import *
from math import *

'''
	 
	 Following is the Binary Tree node structure:
	 
	 class TreeNode:
	     def __init__(self, data=0, left=None, right=None):
	         self.data = data
	         self.left = left
	         self.right = right
'''

def getPreOrderTraversal(root):
	arr = []
	cur = root
	while cur is not None:
		if cur.left is None:
			arr.append(cur.data)
			cur = cur.right
		else:
			prev = cur.left
			while prev.right and prev.right != cur:
				prev = prev.right
			
			if prev.right is None:
				prev.right = cur
				arr.append(cur.data)
				cur = cur.left
			else:
				prev.right = None
				cur = cur.right
	return arr
