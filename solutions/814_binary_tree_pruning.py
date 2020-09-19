# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        """Postorder Traveral.

        Running time: O(n) where n is the number of nodes in the tree.
        """
        def prune(node):
            if not node:
                return True
            
            l = prune(node.left)
            if l:
                node.left = None
            
            r = prune(node.right)
            if r:
                node.right = None

            if l and r and node.val == 0:
                return True
            return False
            
        if prune(root):
            return None
        return root
        
        