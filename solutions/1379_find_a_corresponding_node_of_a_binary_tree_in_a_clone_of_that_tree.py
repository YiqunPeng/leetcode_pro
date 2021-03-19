class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        """Tree.
        """
        path = self._find_path(original, target, [])
        node = cloned
        for p in path:
            if p == 'L':
                node = node.left
            else:
                node = node.right
        return node
    
    def _find_path(self, n, t, path):
        if not n:
            return []
        if n == t:
            return path
        return self._find_path(n.left, t, path + ['L']) or self._find_path(n.right, t, path + ['R'])
