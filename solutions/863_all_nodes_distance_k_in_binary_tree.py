class Solution:
    
    def __init__(self):
        self.g = defaultdict(set)
    
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        self._build_graph(root)
        return self._bfs(target, K)
    
    def _build_graph(self, root):
        q = deque([root])
        while q:
            node = q.popleft()
            if node.left:
                self.g[node].add(node.left)
                self.g[node.left].add(node)
                q.append(node.left)
            if node.right:
                self.g[node].add(node.right)
                self.g[node.right].add(node)
                q.append(node.right)
    
    def _bfs(self, target, K):
        res = []
        q = deque([(target, K)])
        seen = set([target])
        while q:
            node, k = q.popleft()
            if k == 0:
                res.append(node.val)
            if k < 0:
                return res
            for v in self.g[node]:
                if v not in seen:
                    q.append((v, k - 1))
                    seen.add(v)
        return res
