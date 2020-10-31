class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        """Sliding window.

        Running time: O(n) where n == len(S).
        """
        c = collections.Counter(S[:K-1])
        res = 0
        for i in range(K - 1, len(S)):
            if S[i] in c:
                c[S[i]] += 1
            else:
                c[S[i]] = 1
            if len(c) == K:
                res += 1
            c[S[i+1-K]] -= 1
            if c[S[i+1-K]] == 0:
                c.pop(S[i+1-K])
        return res
