class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
    	"""Hash set.
    	"""
        seen = set()
        res = sys.maxsize
        for x1, y1 in points:
            for x2, y2 in seen:
                if (x1, y2) in seen and (x2, y1) in seen:
                    res = min(res, abs((y1 - y2) * (x1 - x2)))
            seen.add((x1, y1))
        return res if res != sys.maxsize else 0
