class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        """Backtracking.
        """
        balance = defaultdict(int)
        for f, t, a in transactions:
            balance[f] -= a
            balance[t] += a
        val = list(balance.values())
        return self._dfs(val, 0, 0)
    
    def _dfs(self, val, start, num):
        while start < len(val) and val[start] == 0:
            start += 1
        if start == len(val):
            return num
        for i in range(start+1, len(val)):
            if val[i] + val[start] == 0:
                val[i] += val[start]
                res = self._dfs(val, start+1, num+1)
                val[i] -= val[start]
                return res
        res = float('inf')
        for i in range(start+1, len(val)):
            if val[i] * val[start] < 0:
                val[i] += val[start]
                res = min(res, self._dfs(val, start+1, num+1))
                val[i] -= val[start]
        return res
