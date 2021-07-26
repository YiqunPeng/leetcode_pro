class Solution:
    
    def __init__(self):
        self.memo = {}
    
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        pres = [0] * n
        pres[-1] = piles[-1]
        for i in range(n - 2, -1, -1):
            pres[i] = pres[i+1] + piles[i]
        return self._dp(0, 1, n, pres)
    
    def _dp(self, i, m, n, pres):
        if (i, m) in self.memo:
            return self.memo[(i, m)]
        res = 0
        if i + 2 * m >= n:
            res = pres[i]
        else:
            for x in range(1, 2 * m + 1):
                res = max(res, pres[i] - self._dp(i+x, max(m, x), n, pres))
        self.memo[(i, m)] = res
        return res
