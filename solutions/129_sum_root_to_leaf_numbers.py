# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
    	"""Postorder traversal.

    	Running time: O(n) where n is the number of nodes in the tree.
    	"""
        def get_sum(node, val):
            if not node:
                return 0
            val = val * 10 + node.val
            if not node.right and not node.left:
                return val
            return get_sum(node.left, val) + get_sum(node.right, val)
                 
        return get_sum(root, 0)