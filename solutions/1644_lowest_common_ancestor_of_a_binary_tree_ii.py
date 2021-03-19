class Solution:
    def __init__(self):
        self.fp = False
        self.fq = False
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = self._lca(root, p, q)
        if self.fp and self.fq:
            return node
        else:
            return None
    
    def _lca(self, node, p, q):
        if not node:
            return None
        left = self._lca(node.left, p, q)
        right = self._lca(node.right, p, q)
        if node == p:
            self.fp = True
            return node
        if node == q:
            self.fq = True
            return node
        if left and right:
            return node
        return left if left else right
