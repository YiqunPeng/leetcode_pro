class Solution:
    
    def __init__(self):
        self.res = []
    
    def combine(self, n: int, k: int) -> List[List[int]]:
        """Backtracking.

        Running time: O(n!).
        """
        self._dfs(1, n + 1, k, [])
        return self.res
    
    def _dfs(self, s, e, k, comb):
        if len(comb) == k:
            self.res.append(comb)
            return
        for i in range(s, e):
            self._dfs(i + 1, e, k, comb + [i])
