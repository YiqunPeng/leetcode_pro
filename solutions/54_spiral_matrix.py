class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    	"""Array.

    	Running time: O(m * n) where m, n are the size of matrix.
    	"""
        m, n = len(matrix), len(matrix[0])
        res = [matrix[0][0]]
        d = 0
        i, j = 0, 0
        min_i, max_i, min_j, max_j = 1, m - 1, 0, n - 1
        while len(res) < m * n:
            if d == 0:
                if j + 1 <= max_j:
                    res.append(matrix[i][j+1])
                    j += 1
                else:
                    d = (d + 1) % 4
                    max_j -= 1
            elif d == 1:
                if i + 1 <= max_i:
                    res.append(matrix[i+1][j])
                    i += 1
                else:
                    d = (d + 1) % 4
                    max_i -= 1
            elif d == 2:
                if j - 1 >= min_j:
                    res.append(matrix[i][j-1])
                    j -= 1
                else:
                    d = (d + 1) % 4
                    min_j += 1
            else:
                if i - 1 >= min_i:
                    res.append(matrix[i-1][j])
                    i -= 1
                else:
                    d = (d + 1) % 4
                    min_i += 1
        return res
