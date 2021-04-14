from heapq import heapify, heappop, heappush

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        """Heap.
        """
        heap = [(0, 0, 0)]
        heapify(heap)
        m, n = len(heights), len(heights[0])
        effort = {(i, j): float('inf') for i in range(m) for j in range(n)}
        effort[(0, 0)] = 0
        while heap:
            e, i, j = heappop(heap)
            if i == m - 1 and j == n - 1:
                return e
            for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:    
                if 0 <= ni < m and 0 <= nj < n:
                    ne = max(e, abs(heights[i][j] - heights[ni][nj]))
                    if ne < effort[(ni, nj)]:
                        effort[(ni, nj)] = ne
                        heappush(heap, (ne, ni, nj))
