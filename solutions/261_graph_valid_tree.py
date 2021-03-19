class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        g = defaultdict(set)
        for a, b in edges:
            g[a].add(b)
            g[b].add(a)
        v = set([0])
        q = deque([0])
        p = {}
        while q:
            node = q.popleft()
            for nei in g[node]:
                if nei in v:
                    if node not in p or p[node] != nei:
                        return False
                else:
                    v.add(nei)
                    q.append(nei)
                    p[nei] = node
        return len(v) == n
