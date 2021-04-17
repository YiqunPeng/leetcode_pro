class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 1, 2 ** 16
        while l <= r:
            m = (l + r) // 2
            c = self._count(m)
            if c <= n and self._count(m + 1) > n:
                return m
            elif c > n:
                r = m - 1
            else:
                l = m + 1
        
    def _count(self, m):
        return (m + 1) * m // 2
