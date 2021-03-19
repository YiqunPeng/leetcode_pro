class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    	"""Heap.

    	Running time: O(klogn) where n == len(nums).
    	"""
        c = collections.Counter(nums)
        h = []
        for kk, v in c.items():
            heapq.heappush(h, (-v, kk))
        res = []
        for i in range(k):
            res.append(heapq.heappop(h)[1])
        return res
