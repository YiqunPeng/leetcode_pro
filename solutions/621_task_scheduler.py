class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = collections.Counter(tasks)
        heap = [(-v, k) for k, v in c.items()]
        res = 0
        while heap:
            ta = []
            for i in range(n + 1):
                if heap:
                    v, k = heapq.heappop(heap)
                    if v + 1 < 0:
                        ta.append((v + 1, k))
                    res += 1
                elif not heap and not ta:
                    return res
                elif not heap and ta:
                    res += n + 1 - i
                    break
            for t in ta:
                heapq.heappush(heap, t)
        return res
