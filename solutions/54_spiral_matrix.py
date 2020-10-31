class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    	"""Array.

    	Running time: O(m * n) where m, n are the size of matrix.
    	"""
        if not matrix:
            return []
        res = []
        k = 0
        m, n = len(matrix), len(matrix[0])
        i, j = 0, 0
        while len(res) < m * n:      
            while j < n - k and len(res) < m * n:
                res.append(matrix[i][j])
                j += 1
            i += 1
            j -= 1
            
            while i < m - k and len(res) < m * n:
                res.append(matrix[i][j])
                i += 1 
            i -= 1
            j -= 1
            
            while j >= k and len(res) < m * n:
                res.append(matrix[i][j])
                j -= 1
            i -= 1
            j += 1
            
            while i > k and len(res) < m * n:
                res.append(matrix[i][j])
                i -= 1  
            i += 1
            j += 1
            
            k += 1
            
        return res
