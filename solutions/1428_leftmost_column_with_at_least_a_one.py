class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        """Two pointers.

        Running time: O(m + n) where m == len(binaryMatrix) and n == len(binaryMatrix[0]).
        """
        m, n = binaryMatrix.dimensions()
        res = n
        row, col = 0, n - 1
        while row < m and col >= 0:
            if binaryMatrix.get(row, col) == 1:
                res = min(res, col)
                col -= 1
            else:
                row += 1
        return res if res < n else -1
