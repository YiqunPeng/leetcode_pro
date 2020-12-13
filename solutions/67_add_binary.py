class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """String.

        Running time: O(n) where n == max(len(a), len(b)).
        """
        res = []
        pa, pb = len(a) - 1, len(b) - 1
        c = 0
        while pa >= 0 or pb >= 0:
            if pa >= 0 and pb >= 0:
                c, v = divmod(int(a[pa]) + int(b[pb]) + c, 2)
                pa -= 1
                pb -= 1
            elif pa >= 0:
                c, v = divmod(int(a[pa]) + c, 2)
                pa -= 1
            else:
                c, v = divmod(int(b[pb]) + c, 2)
                pb -= 1
            res.append(str(v))
        if c:
            res.append(str(c))
        return ''.join(res[::-1])
        