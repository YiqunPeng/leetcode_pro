class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """Heap.
        """
        h = []
        c = Counter(words)
        for kk, v in c.items():
            heapq.heappush(h, (-v, kk))
        res = []
        for i in range(k):
            a, b = heapq.heappop(h)
            res.append(b)
        return res
