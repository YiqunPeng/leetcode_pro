class Solution:
    def reformat(self, s: str) -> str:
        """String.

        Running time: O(n) where n == len(s).
        """
        a, n = [], []
        for i in s:
            if 'a' <= i <= 'z':
                a.append(i)
            else:
                n.append(i)
        if abs(len(a)-len(n)) > 1:
           return ''
        res = ''
        if len(a) < len(n):
            a, n = n, a
        for i in range(len(s)):
            if len(res) % 2 == 0:
                res += a.pop()
            else:
                res += n.pop()
        return res
