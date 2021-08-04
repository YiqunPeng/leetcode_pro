class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        """Tree.
        """
        p_depth = self._get_depth(p)
        q_depth = self._get_depth(q)
        if p_depth < q_depth:
            p_depth, q_depth = q_depth, p_depth
            p, q = q, p
        while p_depth > q_depth:
            p = p.parent
            p_depth -= 1
        while p != q:
            p = p.parent
            q = q.parent
        return p
    
    def _get_depth(self, node):
        n = node
        d = 1
        while n.parent:
            n = n.parent
            d += 1
        return d
