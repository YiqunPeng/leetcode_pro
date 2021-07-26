class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        l1, l2 = len(s1), len(s2)
        dp = [[0] * (l2 + 1) for i in range(l1 + 1)]
        for i in range(l1):
            dp[i+1][0] = dp[i][0] + ord(s1[i])
        for j in range(l2):
            dp[0][j+1] = dp[0][j] + ord(s2[j])
        for i in range(l1):
            for j in range(l2):
                if s1[i] == s2[j]:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    dp[i+1][j+1] = min(dp[i+1][j] + ord(s2[j]), dp[i][j+1] + ord(s1[i]))
        return dp[-1][-1]
