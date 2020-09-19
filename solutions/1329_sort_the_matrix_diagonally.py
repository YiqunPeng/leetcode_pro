class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        """Array.

        Running time: O(nlogn) where n is the size of mat.
        """
        m, n = len(mat), len(mat[0])
        res = [[0] * n for i in range(m)]
        for j in range(n):
            r, c = 0, j
            a = []
            while r < m and c < n:
                a.append(mat[r][c])
                r += 1
                c += 1
            a.sort()
            r, c = 0, j
            for v in a:
                res[r][c] = v
                r += 1
                c += 1
        for i in range(1, m):
            r, c = i, 0
            a = []
            while r < m and c < n:
                a.append(mat[r][c])
                r += 1
                c += 1
            a.sort()
            r, c = i, 0
            for v in a:
                res[r][c] = v
                r += 1
                c += 1
        return res
