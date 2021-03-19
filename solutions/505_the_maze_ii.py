from heapq import heapify, heappush, heappop

class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        """BFS + PQ.
        """
        m, n = len(maze), len(maze[0])
        distance = [[float('inf')] * n for i in range(m)]
        pq = [(0, start[0], start[1])]
        heapify(pq)
        while pq:
            d, i, j = heappop(pq)
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                t = 0
                ci, cj = i, j
                while 0 <= ci+di < m and 0 <= cj+dj < n and maze[ci+di][cj+dj] == 0:
                    t += 1
                    ci += di
                    cj += dj
                if d + t < distance[ci][cj]:
                    distance[ci][cj] = d + t
                    heappush(pq, (d+t, ci, cj))
        if distance[destination[0]][destination[1]] == float('inf'):
            return -1
        else:
            return distance[destination[0]][destination[1]]
