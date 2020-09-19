class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        """Array.

        Running time: O(n) where n is the number of elements in grid.
        """
        if not grid:
            return []
        
        m, n = len(grid), len(grid[0])
        k = k % (m * n)
        
        l = [i for row in grid for i in row]        
        l = l[-k:] + l[:-k]            
        
        res = []
        p = 0
        for i in range(m):
            row = []
            for j in range(n):
                row.append(l[p])
                p += 1
            res.append(row)
            
        return res
        