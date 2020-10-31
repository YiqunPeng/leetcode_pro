class Solution:
    def maxScore(self, s: str) -> int:
        """String.

        Running time: O(n) where n == len(s).
        """
        res = 0
        ones = 0
        for i in s:
            if i == '1':
                ones += 1
        z, o = 0, 0
        for i in s[:-1]:
            if i == '0':
                z += 1
            else:
                o += 1
            res = max(res, z + ones - o)
        return res
