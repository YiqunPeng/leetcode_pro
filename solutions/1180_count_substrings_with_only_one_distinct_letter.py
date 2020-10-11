class Solution:
    def countLetters(self, S: str) -> int:
        """String.

        Running time: O(n) where n == len(S).
        """
        p = 0
        a = S[0]
        res = 0
        n = len(S)
        for i in range(1, n):
            if S[i] != a:
                c = i - p
                res += c * (c + 1) // 2
                a = S[i]
                p = i
        c = n - p
        return res + c * (c + 1) // 2