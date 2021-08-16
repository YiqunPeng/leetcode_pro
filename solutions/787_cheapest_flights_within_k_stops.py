class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        dp = [[float('inf')] * n for i in range(K + 1)]
        for i in range(K + 1):
            dp[i][src] = 0
            for f, t, p in flights:
                if i == 0:
                    if f == src:
                        dp[i][t] = p
                else:
                    if dp[i-1][f] != float('inf'):
                        dp[i][t] = min(dp[i][t], dp[i-1][f] + p)
        return dp[-1][dst] if dp[-1][dst] != float('inf') else -1
