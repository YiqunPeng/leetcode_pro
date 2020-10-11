class Solution:
    def balancedStringSplit(self, s: str) -> int:
        """String.

        Running time: O(n) where n == len(s).
        """
        l, r = 0, 0
        res = 0
        for i in s:
            if i == 'R':
                r += 1
            else:
                l += 1
            if l == r:
                res += 1
                l = r = 0
        return res
