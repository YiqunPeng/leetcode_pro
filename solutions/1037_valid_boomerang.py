class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
    	"""Math - Vector.
		"""
        a, b, c = points
        
        ab = [b[0]-a[0], b[1]-a[1]]
        bc = [c[0]-b[0], c[1]-b[1]]
        
        return ab[1] * bc[0] - bc[1] * ab[0] != 0
 