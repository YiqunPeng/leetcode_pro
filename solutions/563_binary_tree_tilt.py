class Solution:
    
    def __init__(self):
        self.res = 0
    
    def findTilt(self, root: TreeNode) -> int:
        self._post_order(root)
        return self.res
    
    def _post_order(self, root):
        if not root:
            return 0
        lsum = self._post_order(root.left)
        rsum = self._post_order(root.right)
        self.res += abs(lsum - rsum)
        return lsum + rsum + root.val
