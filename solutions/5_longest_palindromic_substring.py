class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[0] * n for i in range(n)]
        for i in range(n):
            dp[i][i] = 1

        l, r = 0, 0
        res = 0
        for d in range(1, n):
            for i in range(0, n - d):
                if s[i] == s[i + d] and (d == 1 or dp[i+1][i+d-1] == 1):
                    dp[i][i+d] = 1
                    if d > res:
                        res = d
                        l, r = i, i + d
        return s[l:r+1]