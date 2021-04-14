from heapq import heappush, heappop, heapify

class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        """Heap.
        """
        heap = [(-A[0][0], 0, 0)]
        heapify(heap)
        visited = set([(0, 0)])
        res = A[0][0]
        while heap:
            v, i, j = heappop(heap)
            res = min(res, -v)
            if i == len(A) - 1 and j == len(A[0]) - 1:
                return res
            for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= ni < len(A) and 0 <= nj < len(A[0]) and (ni, nj) not in visited:
                    visited.add((ni, nj))
                    heappush(heap, (-A[ni][nj], ni, nj))
