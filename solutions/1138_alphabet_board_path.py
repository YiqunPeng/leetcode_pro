class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        """String.

        Running time: O(n) where n == len(target).
        """
        d = {}
        b = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        for i in range(len(b)):
            for j in range(len(b[i])):
                d[b[i][j]] = (i, j)
        res = ''
        x, y = 0, 0
        for t in target:
            nx, ny = d[t]
            if nx < x:
                res += 'U' * (x - nx)
            if ny < y:
                res += 'L' * (y - ny)
            if nx > x:
                res += 'D' * (nx - x)
            if ny > y:
                res += 'R' * (ny - y)
            res += '!'
            x, y = nx, ny
        return res
