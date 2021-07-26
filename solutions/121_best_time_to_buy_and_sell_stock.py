class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """Array.

        Running time: O(n) where n is the length of prices.
        """
        minp = prices[0]
        res = 0
        for p in prices:
            res = max(res, p - minp)
            minp = min(minp, p)
        return res
