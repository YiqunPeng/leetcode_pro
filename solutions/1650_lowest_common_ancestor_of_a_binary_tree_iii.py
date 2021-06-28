class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        """Tree.
        """
        parents = set([p])
        while p.parent:
            parents.add(p.parent)
            p = p.parent
        while q:
            if q in parents:
                return q
            else:
                q = q.parent
