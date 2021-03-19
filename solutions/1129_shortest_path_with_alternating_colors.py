class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        g = {}
        v = set()
        for i, j in red_edges:
            if i not in g:
                g[i] = [set(), set()]
            g[i][0].add(j)
        for i, j in blue_edges:
            if i not in g:
                g[i] = [set(), set()]
            g[i][1].add(j)
        res = [-1] * n
        res[0] = 0
        if 0 not in g:
            return res
        q = deque()
        for nei in g[0][0]:
            q.append((nei, 1, 1))
            v.add((nei, 0))
        for nei in g[0][1]:
            q.append((nei, 0, 1))
            v.add((nei, 1))
        while q:
            node, rb, s = q.popleft()
            if res[node] == -1:
                res[node] = s
            for nei in g.get(node, [set(), set()])[rb]:
                if (nei, rb) not in v:
                    v.add((nei, rb))
                    q.append((nei, 1 - rb, s + 1))
        return res
