class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        depth = self._get_depth(root, 0)
        res = [[""] * (2 ** depth - 1) for i in range(depth)]
        self._print(root, 0, (2 ** depth - 1) // 2, res, 2 ** depth)
        return res
        
    def _get_depth(self, root, d):
        if not root:
            return d
        return 1 + max(self._get_depth(root.left, d), self._get_depth(root.right, d))
    
    def _print(self, root, d, p, res, total):
        res[d][p] = str(root.val)
        diff = total // (2 ** (d + 2))
        if root.left:
            self._print(root.left, d + 1, p - diff, res, total)
        if root.right:
            self._print(root.right, d + 1, p + diff, res, total)
