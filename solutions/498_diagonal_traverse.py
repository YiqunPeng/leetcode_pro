class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        """Array.

        Running time: O(n) where n is the total elements in matrix.
        """
        if not matrix:
            return []
        
        m, n = len(matrix), len(matrix[0])
        d = n + m - 1
        u = 1
        ret = []
        
        for i in range(d):
            if u:
                x = min(i, m - 1)
                y = i - x
                while x >= 0 and y < n:
                    ret.append(matrix[x][y])
                    x -= 1
                    y += 1
            else:
                y = min(i, n - 1)
                x = i - y
                while y >= 0 and x < m:
                    ret.append(matrix[x][y])
                    x += 1
                    y -= 1
            u = 1 - u
        
        return ret
            