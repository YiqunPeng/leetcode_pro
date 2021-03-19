class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        g = defaultdict(set)
        q = deque([root])
        leaves = set()
        start = None
        while q:
            node = q.popleft()
            if node.val == k:
                start = node
            if not node.left and not node.right:
                leaves.add(node)
            if node.left:
                g[node].add(node.left)
                g[node.left].add(node)
                q.append(node.left)
            if node.right:
                g[node].add(node.right)
                g[node.right].add(node)
                q.append(node.right)
        q = deque([start])
        seen = set([start])
        while q:
            node = q.popleft()
            if node in leaves:
                return node.val
            for nxt in g[node]:
                if nxt not in seen:
                    seen.add(nxt)
                    q.append(nxt)
