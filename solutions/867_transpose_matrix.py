class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
    	"""Array.

    	Running time: O(m * n) where m and n are the size of A.
    	"""
        m, n = len(A), len(A[0])
        res = []
        for j in range(n):
            row = []
            for i in range(m):
                row.append(A[i][j])
            res.append(row)
        return res
