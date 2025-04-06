class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """Array.

        Running time: O(n) where n is the length of prices.
        """
        res = 0
        low = prices[0]
        for p in prices[1:]:
            res = max(res, p - low)
            low = min(low, p)
        return res
