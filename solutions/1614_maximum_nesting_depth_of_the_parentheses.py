class Solution:
    def maxDepth(self, s: str) -> int:
        """String.

        Running time: O(n) where n == len(s).
        """
        res = 0
        n = 0
        for i in s:
            if i == '(':
                n += 1
                res = max(res, n)
            elif i == ')':
                n -= 1
        return res
