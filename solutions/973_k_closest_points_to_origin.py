from heapq import heapify, heappush, heappushpop

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """Heap.

        Running time: O(nlogk), where n == len(points).
        """
        heap = []
        heapify(heap)
        for x, y in points:
            d = x * x + y * y
            if len(heap) < k:
                heappush(heap, (-d, x, y))
            else:
                heappushpop(heap, (-d, x, y))
        res = []
        for d, x, y in heap:
            res.append([x, y])
        return res
