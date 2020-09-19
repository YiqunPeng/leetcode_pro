class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
    	"""Tree.

    	Running time: O(h) where h is the height of the tree.
    	"""
        if not root:
            return None
        if not root.left and not root.right:
            return root
        
        left = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(left)
        
        return root