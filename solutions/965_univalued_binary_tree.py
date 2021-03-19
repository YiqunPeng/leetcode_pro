class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool: 
    	"""Recursion.

    	Running time: O(n) where n is the total number of nodes in the tree.
    	"""   
        if not root:
            return True
        l = self.isUnivalTree(root.left)
        r = self.isUnivalTree(root.right)
        if l and r and (not root.left or root.left.val == root.val) and (not root.right or root.right.val == root.val):
            return True
        else:
            return False
