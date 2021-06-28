class Solution:
    
    def __init__(self):
        self.max_sum = float('-inf')
    
    def maxPathSum(self, root: TreeNode) -> int:
        self._root_sum(root)
        return self.max_sum
    
    def _root_sum(self, root):
        if not root:
            return 0
        lsum = max(self._root_sum(root.left), 0)
        rsum = max(self._root_sum(root.right), 0)
        self.max_sum = max(self.max_sum, root.val + lsum + rsum)
        return max(lsum, rsum) + root.val
