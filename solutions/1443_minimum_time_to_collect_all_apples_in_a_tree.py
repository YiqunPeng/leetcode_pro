class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        tree = defaultdict(set)
        for a, b in edges:
            tree[a].add(b)
            tree[b].add(a)
        e = set()
        self._dfs(tree, 0, hasApple, [], set([0]), e)
        return 2 * len(e)
    
    def _dfs(self, tree, node, hasApple, path, seen, e):
        if hasApple[node]:
            for p in path:
                e.add(p)
            path = []
        for child in tree[node]:
            if child not in seen:
                seen.add(child)
                self._dfs(tree, child, hasApple, path + [(node, child)], seen, e)
