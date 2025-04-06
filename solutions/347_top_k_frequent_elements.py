from heapq import heappush, heappop
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    	"""Heap.

    	Running time: O(nlogk) where n == len(nums).
    	"""
        d = Counter(nums)
        
        h = []
        for n, v in d.items():
            heappush(h, (v, n))
            if len(h) > k:
                heappop(h)
        
        res = []
        while h:
            _, n = heappop(h)
            res.append(n)
        return res
