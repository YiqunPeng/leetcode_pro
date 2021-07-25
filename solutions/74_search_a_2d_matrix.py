class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """Binary Search.

        Running time: O(logr + logc) where r is the number of rows and c is the numebr of columns.
        """
        last_val = [row[-1] for row in matrix]
        row_idx = bisect.bisect_left(last_val, target)
        if row_idx == len(matrix):
            return False
        col_idx = bisect.bisect_left(matrix[row_idx], target)
        return matrix[row_idx][col_idx] == target      
        