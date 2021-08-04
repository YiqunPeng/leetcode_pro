class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        return self._lca(root)[1]
    
    def _lca(self, root):
        if not root:
            return 0, None
        l_depth, l_lca = self._lca(root.left)
        r_depth, r_lca = self._lca(root.right)
        if l_depth == r_depth:
            return l_depth + 1, root
        elif l_depth > r_depth:
            return l_depth + 1, l_lca
        else:
            return r_depth + 1, r_lca
