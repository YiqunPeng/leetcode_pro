class Solution:
    def searchMatrix(self, matrix, target):
        """Two pointers.

        Running time: O(r + c) where r is the number of rows and c is the number of columns.
        """
        if not matrix or not matrix[0]:
            return False
        
        r, c = 0, len(matrix[0]) - 1
        
        while r < len(matrix) and c >= 0:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                r += 1
            else:
                c -= 1
                
        return False
