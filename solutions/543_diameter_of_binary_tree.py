class Solution:
    
    def __init__(self):
        self.maxd = 0
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self._post_order(root)
        return self.maxd
    
    def _post_order(self, root):
        if not root:
            return 0
        left = self._post_order(root.left)
        right = self._post_order(root.right)
        self.maxd = max(self.maxd, left + right)
        return max(left, right) + 1
