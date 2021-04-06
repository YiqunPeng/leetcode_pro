class Solution:
    
    def __init__(self):
        self.partitions = []
    
    def partition(self, s: str) -> List[List[str]]:
        self._dfs(s, [])
        return self.partitions
    
    def _dfs(self, s, parts):
        if not s:
            self.partitions.append(parts)
        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:
                self._dfs(s[i:], parts + [s[:i]])
