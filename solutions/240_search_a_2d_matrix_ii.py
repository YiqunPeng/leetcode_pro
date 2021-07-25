class Solution:
    def searchMatrix(self, matrix, target):
        """Two pointers.

        Running time: O(r + c) where r is the number of rows and c is the number of columns.
        """
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1
        while i < m and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            else:
                j -= 1
        return False
