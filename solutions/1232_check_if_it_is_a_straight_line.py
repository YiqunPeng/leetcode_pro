class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
    	"""Math.

    	Running time: O(n) where n == len(coordinates).
    	"""
        for i in range(len(coordinates) - 2):
            a, b, c = coordinates[i], coordinates[i+1], coordinates[i+2]
            ab = (b[0] - a[0], b[1] - a[1])
            bc = (c[0] - b[0], c[1] - b[1])
            if ab[0] * bc[1] != ab[1] * bc[0]:
                return False
        return True
