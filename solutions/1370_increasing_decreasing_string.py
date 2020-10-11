class Solution:
    def sortString(self, s: str) -> str:
        """String.

        Running time: O(n) where n == len(s).
        """
        c = collections.Counter(s)
        l = sorted(c.keys())
        res = ''
        while c:
            for i in l:
                if i in c and c[i] > 0:
                    res += i
                    c[i] -= 1
                    if c[i] == 0:
                        c.pop(i)
            l.reverse()
        return res
