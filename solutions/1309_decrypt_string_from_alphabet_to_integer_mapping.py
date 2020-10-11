class Solution:
    def freqAlphabets(self, s: str) -> str:
        """String.

        Running time: O(n) where n == len(s).
        """
        p = 0
        res = ''
        while p < len(s):
            if p + 2 < len(s) and s[p+2] == '#':
                res += chr(ord('a') + int(s[p:p+2]) - 1)
                p += 3
            else:
                res += chr(ord('a') + int(s[p]) - 1)
                p += 1
        return res
