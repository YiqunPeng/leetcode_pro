class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """Array.

        Running time: O(n) where n is the length of prices.
        """
        if not prices:
            return 0
        n = len(prices)
        res = 0
        m = prices[0]
        for i in range(1, n):
            res = max(res, prices[i] - m)
            m = min(m, prices[i])
        return res
