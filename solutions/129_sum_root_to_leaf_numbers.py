class Solution:
    
    def __init__(self):
        self.s = 0
    
    def sumNumbers(self, root: TreeNode) -> int:
        self._sum(root, 0)
        return self.s
        
    def _sum(self, root, v):
        if not root:
            return
        if not root.left and not root.right:
            self.s += v * 10 + root.val
            return
        self._sum(root.left, v * 10 + root.val)
        self._sum(root.right, v * 10 + root.val)
