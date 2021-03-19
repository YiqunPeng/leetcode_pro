class Solution:
    def countNodes(self, root: TreeNode) -> int:
        """Tree.

        Running time: O(logn ^ 2).
        """
        if not root:
            return 0
        h = self._height(root)
        rh = self._height(root.right)
        if rh == h - 1:
            return 2 ** rh + self.countNodes(root.right)
        else:
            return 2 ** rh + self.countNodes(root.left)
    
    def _height(self, root):
        if not root:
            return 0
        return 1 + self._height(root.left)
