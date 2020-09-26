class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
    	"""Hash set.

    	Running time: O(k) where k is the number of items in matrix.
    	"""
        r_min = {min(row) for row in matrix}
        c_max = {max(col) for col in zip(*matrix)}
        return list(r_min & c_max)
