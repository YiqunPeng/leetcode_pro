class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        """Hash table.
        """
        res = 0
        for x1, y1 in points:
            d = {}
            for x2, y2 in points:
                dis = (x1 - x2) ** 2 + (y1 - y2) ** 2
                if dis not in d:
                    d[dis] = 1
                else:
                    res += d[dis]
                    d[dis] += 1
        return res * 2
