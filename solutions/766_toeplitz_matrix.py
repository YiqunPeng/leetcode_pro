class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        """Hash table.

        Running time: O(mn) where m, n are the size of matrix.
        """
        m, n = len(matrix), len(matrix[0])
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] != matrix[i-1][j-1]:
                    return False
        return True
