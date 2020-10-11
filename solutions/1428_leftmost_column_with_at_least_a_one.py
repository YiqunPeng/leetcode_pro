class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        """Two pointers.

        Running time: O(m + n) where m == len(binaryMatrix) and n == len(binaryMatrix[0]).
        """
        m, n = binaryMatrix.dimensions()
        maxv = 0
        res = -1
        j = n - 1
        for i in range(m):
            while j >= 0 and binaryMatrix.get(i, j) == 1:
                j -= 1
            if n - 1 - j > maxv:
                maxv = n - 1 - j
                res = j + 1
        return res
