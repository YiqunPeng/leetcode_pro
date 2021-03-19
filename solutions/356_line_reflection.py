class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        """Hash set.
        """
        s = set()
        mi, ma = sys.maxsize, -sys.maxsize
        for x, y in points:
            s.add((x, y))
            mi = min(mi, x)
            ma = max(ma, x)
        for x, y in points:
            t = mi + ma - x
            if (t, y) not in s:
                return False
        return True
