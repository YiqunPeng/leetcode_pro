class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
    	"""Heap.

    	Running time: O(nlogn) where n is the number of stones.
    	"""
        from heapq import heappush, heappop, heapify
        
        heap = [-s for s in stones]
        heapify(heap)
        
        while len(heap) > 1:
            a, b = heappop(heap), heappop(heap)
            if a != b:
                heappush(heap, a - b)
                
        return -heappop(heap) if heap else 0