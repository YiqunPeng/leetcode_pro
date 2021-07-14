class Solution:
    
    def __init__(self):
        self.graph = defaultdict(list)
        self.memo = defaultdict(float)
    
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        for i in range(len(equations)):
            a, b, v = equations[i][0], equations[i][1], values[i]
            self.graph[a].append((b, v))
            self.graph[b].append((a, 1 / v))
            self.memo[(a, b)] = v
            self.memo[(b, a)] = 1 / v
            self.memo[(a, a)] = self.memo[(b, b)] = 1.0
        res = []
        for a, b in queries:
            if a not in self.graph or b not in self.graph:
                res.append(-1.0)
                continue
            if (a, b) in self.memo:
                res.append(self.memo[(a, b)])
            else:
                res.append(self._dfs(a, a, b, 1.0, set([a])))
        return res

    def _dfs(self, a, curr, b, val, seen):
        if curr == b:
            self.memo[(a, b)] = val
            return val
        for n, d in self.graph[curr]:
            if n not in seen:
                seen.add(n)
                self.memo[(a, n)] = val * d
                res = self._dfs(a, n, b, val * d, seen)
                seen.remove(n)
                if res != -1.0:
                    return res
        return -1.0