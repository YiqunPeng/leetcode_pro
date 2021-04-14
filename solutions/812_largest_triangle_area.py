class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        area = 0.0
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                for k in range(j+1, len(points)):
                    a, b, c = points[i], points[j], points[k]
                    ab = (points[j][0] - points[i][0], points[j][1] - points[i][1])
                    ac = (points[k][0] - points[i][0], points[k][1] - points[i][1])
                    area = max(area, abs(ab[0] * ac[1] - ab[1] * ac[0]) * 0.5)
        return area
