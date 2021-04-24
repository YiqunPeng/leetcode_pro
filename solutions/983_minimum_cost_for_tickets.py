class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        fday, lday = days[0], days[-1]
        dp = [float('inf')] * (lday - fday + 2)
        dp[0] = 0
        days = set(days)
        for i in range(lday - fday + 1):
            if fday + i not in days:
                dp[i+1] = dp[i]
                continue
            dp[i+1] = min(dp[i] + costs[0], dp[max(0, i-6)] + costs[1], dp[max(0, i-29)] + costs[2])
        return dp[-1]
