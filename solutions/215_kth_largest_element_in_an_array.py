from heapq import heapify, heappush, heappushpop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """Heap.

        Runninng time: O(nlogk) where n == len(nums).
        """
        heap = []
        heapify(heap)
        for num in nums:
            if len(heap) < k:
                heappush(heap, num)
            else:
                heappushpop(heap, num)
        return heappop(heap)
