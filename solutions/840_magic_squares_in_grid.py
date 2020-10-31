class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        """Array.

        Running time: O(m * n) where m, n are the size of grid.
        """
        m, n = len(grid), len(grid[0])
        if m < 3 or n < 3:
            return 0
        candid = set()
        for i in range(m - 2):
            for j in range(n - 2):
                r = sum([grid[i][j], grid[i][j+1], grid[i][j+2]])
                c = sum([grid[i][j], grid[i+1][j], grid[i+2][j]])
                d = sum([grid[i][j], grid[i+1][j+1], grid[i+2][j+2]])
                sd = sum([grid[i+2][j], grid[i+1][j+1], grid[i][j+2]])
                if r == c == d == sd == 15:
                    candid.add((i, j))
                if r != 15:
                    candid.discard((i - 1, j))
                    candid.discard((i - 2, j))
                if c != 15:
                    candid.discard((i, j - 1))
                    candid.discard((i, j - 2))
        return len([i for i in candid if self._is_1_to_9(grid, i)])
                    
    def _is_1_to_9(self, grid, i):
        x, y = i[0], i[1]
        n = set([i for i in range(1, 10)])
        for i in range(3):
            for j in range(3):
                n.discard(grid[x+i][y+j])
        return len(n) == 0
