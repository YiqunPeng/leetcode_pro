class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
    	"""Tree.

    	Running time: O(h) where h is the height of the tree.
    	"""
        if not root:
            return None
        root.right, root.left = root.left, root.right
        self.invertTree(root.right)
        self.invertTree(root.left)
        return root
