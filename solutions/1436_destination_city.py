class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
    	"""Hash set.

    	Running time: O(n) where n == len(paths).
    	"""
        s = set([p[0] for p in paths])
        for p in paths:
            if p[1] not in s:
                return p[1]
