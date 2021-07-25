class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        """Two pointers.

        Running time: O(m + n) where m == len(binaryMatrix) and n == len(binaryMatrix[0]).
        """
        m, n = binaryMatrix.dimensions()
        j = n
        for i in range(m):
            idx = self._binary_search(binaryMatrix, i, 0, j)
            if idx < j:
                j = idx
        return j if j < n else -1
    
    def _binary_search(self, m, row, lo, hi):
        while lo < hi:
            mi = (lo + hi) // 2
            if m.get(row, mi) < 1:
                lo = mi + 1
            else:
                hi = mi
        return lo
