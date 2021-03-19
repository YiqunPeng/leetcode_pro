class Solution:
    def checkEquivalence(self, root1: 'Node', root2: 'Node') -> bool:
        l1 = self._get_leaves(root1)
        l2 = self._get_leaves(root2)
        return l1 == l2
    
    def _get_leaves(self, root):
        leaves = defaultdict(int)
        q = deque([root])
        while q:
            node = q.popleft()
            if not node.left and not node.right:
                leaves[node.val] += 1
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return leaves
