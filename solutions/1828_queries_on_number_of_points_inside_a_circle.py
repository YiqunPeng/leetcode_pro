class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = []
        for x, y, r in queries:
            cnt = 0
            for i, j in points:
                if (x - i) ** 2 + (y - j) ** 2 <= r ** 2:
                    cnt += 1
            res.append(cnt)
        return res
