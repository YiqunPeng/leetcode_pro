from heapq import heappush, heappop

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        """Heap.

        Running time: O(n^2 logn) where n == len(grid).
        """
        res = 0
        n = len(grid)
        heap = [(grid[0][0], 0, 0)]
        visited = set([(0, 0)])
        while heap:
            v, i, j = heappop(heap)
            res = max(res, v)
            if i == j == n - 1:
                return res
            for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= ni < n and 0 <= nj < n and (ni, nj) not in visited:
                    visited.add((ni, nj))
                    heappush(heap, (grid[ni][nj], ni, nj))
