class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        """String.

        Running time: O(n) where n is the length S.
        """
        left = 0
        res = 0
        for p in s:
            if p == '(':
                left += 1
            else:
                if left == 0:
                    res += 1
                else:
                    left -= 1
        return res + left
