class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        """Array.

        Running time: O(k) where k is the number of elements in grid.
        """
        m, n = len(grid), len(grid[0])
        res = 0
        j = 0
        for i in range(m):
            if grid[i][j] >= 0:
                while j < n and grid[i][j] >= 0:
                    j += 1
            else:
                while j - 1 >= 0 and grid[i][j-1] < 0:
                    j -= 1
            res += n - j
            j = min(n - 1, j)
        return res
