class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        """Array.

        Running time: O(m * n) where m and n are the size of picture.
        """
        m, n = len(picture), len(picture[0])
        row, col = [0] * m , [0] * n
        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B':
                    row[i] += 1
                    col[j] += 1
        res = 0
        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B' and row[i] == col[j] == 1:
                    res += 1
        return res
