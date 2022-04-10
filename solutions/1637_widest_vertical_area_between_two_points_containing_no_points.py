class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x = sorted([p[0] for p in points])
        res = 0
        for i in range(1, len(x)):
            res = max(res, x[i] - x[i-1])
        return res
