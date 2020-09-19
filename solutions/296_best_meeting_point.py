class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        """Math.

        Running time: O(klogk) where k is the area of the grid.
        """
        if not grid:
            return 0
        
        rows, cols = [], []
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    rows.append(i)
                    cols.append(j)
        
        rows.sort()
        cols.sort()
        
        row = rows[len(rows)//2]
        col = cols[len(cols)//2]
                
        ret = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ret += abs(row - i) + abs(col - j)
        return ret