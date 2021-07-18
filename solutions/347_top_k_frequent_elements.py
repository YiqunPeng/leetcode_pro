from heapq import heappush, heappop, heapify

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    	"""Heap.

    	Running time: O(nlogk) where n == len(nums).
    	"""
        counter = Counter(nums)
        heap = []
        heapify(heap)
        for kk, v in counter.items():
            heappush(heap, (v, kk))
            if len(heap) > k:
                heappop(heap)
        res = []
        for i in range(len(heap)):
            res.append(heap[i][1])
        return res
