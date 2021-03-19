class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        """Hash table.
        """
        p = {}
        dp = {}
        d = 0
        cells = tuple(cells)
        while d < N and cells not in p:
            p[cells] = d
            dp[d] = cells
            ncells = [0] * 8
            for i in range(1, 7):
                if cells[i-1] == cells[i+1]:
                    ncells[i] = 1
            cells = tuple(ncells)
            d += 1
        if d == N:
            return cells
        else:
            return dp[p[cells]+(N-d)%(d-p[cells])]
