class Solution:
    def checkEqualTree(self, root: TreeNode) -> bool:
        s = self._get_sum(root)
        if s % 2 == 1:
            return False
        ls, lp = self._partition(root.left, s // 2)
        rs, rp = self._partition(root.right, s // 2)
        return lp or rp
    
    def _get_sum(self, root):
        if not root:
            return 0
        return root.val + self._get_sum(root.left) + self._get_sum(root.right)
    
    def _partition(self, root, target):
        if not root:
            return 0, False
        ls, lp = self._partition(root.left, target)
        rs, rp = self._partition(root.right, target)
        v = ls + rs + root.val
        return v, lp or rp or v == target
