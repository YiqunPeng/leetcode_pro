class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s:
            return not t
        return self._equals(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        
    def _equals(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        return s.val == t.val and self._equals(s.left, t.left) and self._equals(s.right, t.right)
