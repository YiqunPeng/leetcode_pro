class Solution:
    def numWays(self, s: str) -> int:
        """Math.

        Running time: O(n) where n == len(s).
        """
        one = 0
        m = 10 ** 9 + 7
        for i in s:
            if i == '1':
                one += 1
        if one % 3 != 0:
            return 0
        if one == 0:
            return (len(s) - 1) * (len(s) - 2) // 2 % m
        o = 0
        res = 1
        p = 0
        for i, c in enumerate(s):
            if c == '1':
                if o and o % (one // 3) == 0:
                    res = (res * (i - p)) % m
                p = i
                o += 1
        return res
