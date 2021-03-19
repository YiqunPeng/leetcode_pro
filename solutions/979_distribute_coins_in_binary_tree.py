class Solution:
    
    def __init__(self):
        self.res = 0
    
    def distributeCoins(self, root: TreeNode) -> int:
        self._post_order(root)
        return self.res
    
    def _post_order(self, root):
        if not root:
            return 0
        l = self._post_order(root.left)
        r = self._post_order(root.right)
        self.res += abs(l) + abs(r)
        return root.val - 1 + l + r
