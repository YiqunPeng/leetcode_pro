class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """DP.
        """
        d = set(wordDict)
        n = len(s)
        dp = [[] for i in range(n)]
        if s[0] in d:
            dp[0] = [[s[0]]]
        for i in range(1, n):
            if s[:i+1] in d:
                dp[i] = [[s[:i+1]]]
            for j in range(0, i):
                if dp[j] and s[j+1:i+1] in d:
                    for k in dp[j]:
                        dp[i].append(k + [s[j+1:i+1]])
        res = []
        for k in dp[-1]:
            res.append(' '.join(k))
        return res
