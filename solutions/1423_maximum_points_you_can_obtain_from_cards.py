class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        """Prefix sum.
        """
        n = len(cardPoints)
        res = s = sum(cardPoints[:k])
        for i in range(n-1, n-k-1, -1):
            s = s + cardPoints[i] - cardPoints[i-n+k]
            res = max(res, s)
        return res
