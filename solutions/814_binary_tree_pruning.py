class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        """Postorder Traveral.

        Running time: O(n) where n is the number of nodes in the tree.
        """
        if not root:
            return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if root.left or root.right or root.val == 1:
            return root
        return None
