class Solution:
    def countLargestGroup(self, n: int) -> int:
        """Array.

        Running time: O(n).
        """
        d = collections.defaultdict(int)
        for i in range(1, n + 1):
            s = self._sum(i)
            d[s] += 1
        m = -1
        res = 0
        for v in d.values():
            if v > m:
                res = 1
                m = v
            elif v == m:
                res += 1
        return res
    
    def _sum(self, i):
        s = 0
        while i > 0:
            s += i % 10
            i //= 10
        return s
