# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        """Iterative

		Running Time: O(h) where h is the height of the BST.
        """
        succ = None
        
        while root:
            if p.val < root.val:
                succ = root
                root = root.left
            else:
                root = root.right
                
        return succ

    def inorderSuccessor_2(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        """Recursive

		Running Time: O(h) where h is the height of the BST.
		"""
        if not root:
            return None
        
        if p.val < root.val:
            left = self.inorderSuccessor(root.left, p)
            return left if left else root
        else:
            return self.inorderSuccessor(root.right, p)
