from heapq import heappush, heappop, heapify

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        """Priority queue.

        Running time: O(mnlogmn) where m, n are the size of heightMap.
        """
        if not heightMap:
            return 0
        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for i in range(m)]
        pq = []
        heapify(pq)
        res = 0
        for i in range(m):
            heappush(pq, [heightMap[i][0], i, 0])
            heappush(pq, [heightMap[i][n-1], i, n-1])
            visited[i][0] = visited[i][n-1] = True
        for j in range(n):
            heappush(pq, [heightMap[0][j], 0, j])
            heappush(pq, [heightMap[m-1][j], m-1, j])
            visited[0][j] = visited[m-1][j] = True
        while pq:
            h, i, j = heappop(pq)
            for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= ni < m and 0 <= nj < n and not visited[ni][nj]:
                    visited[ni][nj] = True
                    res += max(0, h - heightMap[ni][nj])
                    heappush(pq, [max(h, heightMap[ni][nj]), ni, nj])
        return res
