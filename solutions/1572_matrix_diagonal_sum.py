class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
    	"""Array.

    	Running time: O(n) where n is the size of the mat.
    	"""
        res = 0
        n = len(mat)
        for i in range(n):
            res += mat[i][i]
            if i != n - 1 - i:
                res += mat[i][n-1-i]
        return res
