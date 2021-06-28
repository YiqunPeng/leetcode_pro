class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        """Backtracking.
        """
        return self._dfs(n, n)

    def _dfs(self, n, curr):
        if curr == 0:
            return ['']
        if curr == 1:
            return ['0', '1', '8']
        parts = self._dfs(n, curr - 2)
        res = []
        for part in parts:
            if curr != n:
                res.append('0' + part + '0')
            res.append('1' + part + '1')
            res.append('6' + part + '9')
            res.append('8' + part + '8')
            res.append('9' + part + '6')
        return res
