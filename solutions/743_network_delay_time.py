from heapq import heapify, heappush, heappop

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(defaultdict)
        delay = {i: float('inf') for i in range(1, n + 1)}
        delay[k] = 0
        for u, v, w in times:
            graph[u][v] = w
        pq = []
        heappush(pq, (0, k))
        while pq:
            t, node = heappop(pq)
            for nei in graph[node]:
                v = graph[node][nei] + t
                if v < delay[nei]:
                    delay[nei] = v
                    heappush(pq, (v, nei))
        res = 0
        for v in delay.values():
            if v == float('inf'):
                return -1
            res = max(res, v)
        return res
