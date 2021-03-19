class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        d = {0: 1}
        return self._find_all_paths(root, 0, sum, d)
        
    def _find_all_paths(self, root, pres, s, d):
        if not root:
            return 0
        curr = pres + root.val
        res = d.get(curr - s, 0)
        d[curr] = d.get(curr, 0) + 1
        res += self._find_all_paths(root.left, curr, s, d) + self._find_all_paths(root.right, curr, s, d)
        d[curr] -= 1
        return res
