class Solution:
    
    def __init__(self):
        self.s = 0
    
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self._search(root, low, high)
        return self.s
    
    def _search(self, root, l, h):
        if not root:
            return 0
        if root.val < l:
            self._search(root.right, l, h)
        elif root.val > h:
            self._search(root.left, l, h)
        else:
            self.s += root.val
            self._search(root.right, l, h)
            self._search(root.left, l, h)
