class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        """Array.

        Running time: O(n) where n is the number of grids.
        """
        a = 0
        m, n = len(grid), len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    a += 2
                if not i:
                    a += grid[i][j]    
                else:
                    a += abs(grid[i-1][j] - grid[i][j])
                if i == m - 1:
                    a += grid[i][j]
                    
                if not j:
                    a += grid[i][j]
                else:
                    a += abs(grid[i][j-1] - grid[i][j])
                if j == n - 1:
                    a += grid[i][j]
        
        return a