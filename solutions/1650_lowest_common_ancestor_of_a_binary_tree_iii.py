class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        """Tree.
        """
        p_parents = set([p])
        node = p
        while node.parent:
            p_parents.add(node.parent)
            node = node.parent
        node = q
        while node not in p_parents:
            node = node.parent
        return node
