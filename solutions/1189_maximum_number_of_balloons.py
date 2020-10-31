class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        """Hash table.

        Running time: O(n) where n == len(text).
        """
        c = collections.Counter(text)
        res = sys.maxsize
        d = {'b': 1, 'a': 1, 'l': 2, 'o': 2, 'n': 1}
        for k, v in d.items():
            if k not in c:
                return 0
            else:
                res = min(res, c[k] // v)
        return res
