class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        """String.

        Running time: O(n) where n == len(s).
        """
        c = 1
        pc = 0
        res = 0
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                c += 1
            else:
                pc = c
                c = 1
            if c <= pc:
                res += 1
        return res
