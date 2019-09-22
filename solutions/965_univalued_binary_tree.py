# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool: 
    	"""Recursion.

    	Running time: O(n) where n is the total number of nodes in the tree.
    	"""   
        res = True
        
        if root.left:
            res = root.val == root.left.val and self.isUnivalTree(root.left)
        
        if root.right:
            res = res and root.val == root.right.val and self.isUnivalTree(root.right)

        return res