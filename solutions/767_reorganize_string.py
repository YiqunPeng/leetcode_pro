class Solution:
    def reorganizeString(self, S: str) -> str:
        """Heap.

        Running time:O(nlogn) where n is the length of S.
        """
        c = collections.Counter(S)
        heap = [(-v, k) for k, v in c.items()]
        heapq.heapify(heap)
        res = ''
        while heap:
            v, k = heapq.heappop(heap)
            if not res or res[-1] != k:
                res += k
                if -v > 1:
                    heapq.heappush(heap, (v+1, k))
            else:
                if not heap:
                    return ''
                vv, kk = heapq.heappop(heap)
                res += kk
                if -vv > 1:
                    heapq.heappush(heap, (vv+1, kk))
                heapq.heappush(heap, (v, k))
        return res  
