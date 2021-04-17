class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        ab = (points[1][0] - points[0][0], points[1][1] - points[0][1])
        bc = (points[2][0] - points[1][0], points[2][1] - points[1][1])
        return ab != (0, 0) and bc != (0, 0) and ab[0] * bc[1] != ab[1] * bc[0]
