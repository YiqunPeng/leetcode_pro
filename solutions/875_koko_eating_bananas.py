class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """Binary search.
        """
        l, r = 1, max(piles)
        while l < r:
            k = (l + r) // 2
            hours = self.count_hours(piles, k)
            if hours <= h:
                r = k
            else:
                l = k + 1
        return l

    def count_hours(self, piles, k):
        t = 0
        for p in piles:
            if p % k == 0:
                t += p // k
            else:
                t += p // k + 1
        return t
