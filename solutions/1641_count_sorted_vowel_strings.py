class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [[0, 0, 0, 0, 0] for i in range(n)]
        dp[0] = [1, 1, 1, 1, 1]
        d = {0: 5, 1: 4, 2: 3, 3: 2, 4: 1}
        for i in range(1, n):
            for j in range(5):
                for k in range(j+1):
                    dp[i][k] += dp[i-1][j]
        return sum(dp[-1])
