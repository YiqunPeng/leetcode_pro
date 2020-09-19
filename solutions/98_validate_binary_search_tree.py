# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
    	"""BST.

    	Running time: O(n) where n is the number of nodes in the BST.
    	"""
        def is_valid(node, l, r):
            if not node:
                return True
            if node.val <= l or node.val >= r:
                return False
            
            return is_valid(node.left, l, node.val) and is_valid(node.right, node.val, r)
        
        return is_valid(root, -sys.maxsize, sys.maxsize)