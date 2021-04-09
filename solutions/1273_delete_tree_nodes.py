class Solution:
    
    def __init__(self):
        self.tree = defaultdict(set)
    
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        for i in range(len(parent)):
            self.tree[parent[i]].add(i)
        return self._dfs(0, value)[0]
    
    def _dfs(self, node, value):
        cnt, val = 1, value[node]
        for child in self.tree[node]:
            c, v = self._dfs(child, value)
            cnt += c
            val += v
        return cnt if val != 0 else 0, val
