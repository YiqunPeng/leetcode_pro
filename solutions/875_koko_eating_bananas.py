class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """Binary search.
        """
        l, r = 1, max(piles)
        while l < r:
            m = (l + r) // 2
            if self._can_finish(m, h, piles):
                r = m
            else:
                l = m + 1
        return l
    
    def _can_finish(self, k, h, piles):
        v = 0
        for p in piles:
            v += (p - 1) // k + 1
        return v <= h
