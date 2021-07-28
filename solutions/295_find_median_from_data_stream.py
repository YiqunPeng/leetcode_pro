from heapq import heappush, heappop, heapify

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heap = [] # 2nd half
        self.max_heap = [] # 1st half
        heapify(self.min_heap)
        heapify(self.max_heap)

    def addNum(self, num: int) -> None:
        if not self.max_heap or num <= -self.max_heap[0]:
            heappush(self.max_heap, -num)
            if len(self.max_heap) - len(self.min_heap) > 1:
                heappush(self.min_heap, -heappop(self.max_heap))
        else:
            heappush(self.min_heap, num)
            if len(self.min_heap) - len(self.max_heap) > 1:
                heappush(self.max_heap, -heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        elif len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0] / 1.0
        else:
            return -self.max_heap[0] / 1.0
