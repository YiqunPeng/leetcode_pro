class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        m, n = len(grid), len(grid[0]) 
        peri = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    peri += 4                  
                    if i and grid[i-1][j] == 1:
                        peri -= 2
                    if j and grid[i][j-1] == 1:
                        peri -= 2
        
        return peri
