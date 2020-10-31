class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """Array.

        Running time: O(n * m) where n and m are the size of matrix.
        """
        fr, fc = False, False
        m, n = len(matrix), len(matrix[0])
        for j in range(n):
            if matrix[0][j] == 0:
                fr = True
                break
        for i in range(m):
            if matrix[i][0] == 0:
                fc = True
                break
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if fr:
            for j in range(n):
                matrix[0][j] = 0
        if fc:
            for i in range(m):
                matrix[i][0] = 0
