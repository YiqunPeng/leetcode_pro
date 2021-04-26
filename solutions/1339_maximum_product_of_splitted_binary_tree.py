class Solution:
    
    def __init__(self):
        self.s = []
        self.mod = 10 ** 9 + 7
    
    def maxProduct(self, root: TreeNode) -> int:
        t = self._postorder(root)
        return max((t - i) * i for i in self.s) % self.mod 
    
    def _postorder(self, root):
        if not root:
            return
        lsum, rsum = 0, 0
        if root.left:
            lsum = self._postorder(root.left)
            self.s.append(lsum)
        if root.right:
            rsum = self._postorder(root.right)
            self.s.append(rsum)
        t = lsum + rsum + root.val
        self.s.append(t)
        return t
