class MovingAverage:

    def __init__(self, size: int):
        """Running time: O(1).
        """
        self.size = size
        self.arr = collections.deque([])
        self.sum = 0
        

    def next(self, val: int) -> float:
        """Queue.
    
        Running time: O(1).
        """
        if len(self.arr) < self.size:
            self.sum += val
            self.arr.append(val)
            return self.sum / len(self.arr)
        else:
            self.sum = self.sum - self.arr[0] + val
            self.arr.popleft()
            self.arr.append(val)
            return self.sum / self.size
