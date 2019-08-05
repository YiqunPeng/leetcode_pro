# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
    	"""DFS.
	
		Running time: O(n) where n is the total amount of nodes in both trees.
    	"""
        def find_leaves(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [node.val]
            
            return find_leaves(node.left) + find_leaves(node.right)

        return find_leaves(root1) == find_leaves(root2)