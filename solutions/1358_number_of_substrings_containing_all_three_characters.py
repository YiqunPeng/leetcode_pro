class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        """Hash table.

        Running time: O(n) where n == len(s).
        """
        d = {'a': -1, 'b': -1, 'c': -1}
        res = 0
        for i, c in enumerate(s):
            d[c] = i
            if c == 'a':
                idx = min(d['b'], d['c'])
            elif c == 'b':
                idx = min(d['a'], d['c'])
            else:
                idx = min(d['a'], d['b'])
            res += idx + 1
        return res
