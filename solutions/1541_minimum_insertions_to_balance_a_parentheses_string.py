class Solution:
    def minInsertions(self, s: str) -> int:
        """String.

        Running time: O(n) where n == len(s).
        """
        res = 0
        r = 0
        for c in s:
            if c == '(':
                if r % 2 == 1:
                    r -= 1
                    res += 1
                r += 2
            else:
                r -= 1
                if r < 0:
                    r += 2
                    res += 1
        return res + r
