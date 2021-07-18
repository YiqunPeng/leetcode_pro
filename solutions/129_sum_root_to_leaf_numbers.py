class Solution:
    
    def __init__(self):
        self.s = 0
    
    def sumNumbers(self, root: TreeNode) -> int:
        self._traverse(root, 0)
        return self.s
    
    def _traverse(self, root, val):
        if not root:
            return
        val = val * 10 + root.val
        if not root.left and not root.right:
            self.s += val
        self._traverse(root.left, val)
        self._traverse(root.right, val)
