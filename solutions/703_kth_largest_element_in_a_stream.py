import heapq

class KthLargest:
    """Heap.

    Running time: O(nlogk) where n is the total number of elements in the stream.
    """

    def __init__(self, k: int, nums: List[int]):
        self.k = k        
        self.heap = []
        
        for num in nums:
            self.add(num)
        
    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        else:
            heapq.heappushpop(self.heap, val)
        return self.heap[0]
