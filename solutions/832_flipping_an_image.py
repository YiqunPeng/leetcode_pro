class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        """Array.

        Running time: O(n) where n is the size of A.
        """
        n = len(A)
        res = [[0] * n for i in range(n)]
        for i in range(n):
            for j in range(n):
                res[i][j] = 1 - A[i][n-1-j]
        return res