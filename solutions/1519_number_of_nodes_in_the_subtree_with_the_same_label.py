class Solution:
    
    def __init__(self):
        self.res = []
        self.g = defaultdict(set)
    
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        self.res = [1] * n
        self._construct_graph(edges)
        self._dfs(labels, 0, None)
        return self.res
        
    def _construct_graph(self, edges):
        for a, b in edges:
            self.g[a].add(b)
            self.g[b].add(a)
            
    def _dfs(self, labels, node, parent):
        ret = {}
        for nei in self.g[node]:
            if nei != parent:
                sub = self._dfs(labels, nei, node)
                for k in sub:
                    ret[k] = ret.get(k, 0) + sub[k]
        self.res[node] = ret.get(labels[node], 0) + 1
        ret[labels[node]] = self.res[node]
        return ret
