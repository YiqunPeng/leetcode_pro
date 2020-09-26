class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        """Array.

        Running time: O(mn) where m, n are the size of mat.
        """
        m, n = len(mat), len(mat[0])
        row = [sum(i) for i in mat]
        col = [sum(i) for i in zip(*mat)]
        res = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and row[i] == 1 and col[j] == 1:
                    res += 1
        return res
