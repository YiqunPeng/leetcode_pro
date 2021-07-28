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
        prev = None
        while root:
            if root.val > p.val:
                prev = root
                root = root.left
            else:
                root = root.right
        return prev
