class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        q = [(0, 0, (0, 0))]
        v = set([(0, 0)])
        while q:
            r, s, (i, j) = heapq.heappop(q)
            if i == x and j == y:
                return s
            for ni, nj in [(i-2, j+1), (i-1, j+2), (i+1, j+2), (i+2, j+1), (i+2, j-1), (i+1, j-2), (i-1, j-2), (i-2, j-1)]:
                if (ni, nj) not in v:
                    v.add((ni, nj))
                    heapq.heappush(q, (s + 1 + self._rank(ni, nj, x, y), s + 1, (ni, nj)))
    
    def _rank(self, x1, y1, x, y):
        return sqrt((x1 - x) ** 2 + (y1 - y) ** 2)
