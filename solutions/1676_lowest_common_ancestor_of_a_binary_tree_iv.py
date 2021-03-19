class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        nodes = set(nodes)
        return self._lca(root, nodes)
    
    def _lca(self, root, nodes):
        if not root or root in nodes:
            return root
        l = self._lca(root.left, nodes)
        r = self._lca(root.right, nodes)
        if l and r:
            return root
        return l if l else r
