class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        """String

        Running time: O(n) where n == len(s).
        """
        m = [0] * 26
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            d = (ord(t[i]) - ord(s[i]) + 26) % 26
            if d and (d > k or d + 26 * m[d] > k):
                return False
            m[d] += 1
        return True
