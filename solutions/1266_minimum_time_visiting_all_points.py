class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
    	"""Array.

    	Running time: O(n) where n is the number of points.
    	"""
        res = 0
        sx, sy = points[0][0], points[0][1]
        for ex, ey in points[1:]:
            dx = abs(sx - ex)
            dy = abs(sy - ey)
            res += min(dx, dy) + abs(dx - dy)
            sx, sy = ex, ey
        return res
