class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.q = [None] * k
        self.h = 0
        self.t = 0
        self.k = k
        self.c = 0

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        
        Running time: O(1).
        """
        if not self.isFull():
            self.q[self.t] = value
            self.t = (self.t + 1) % self.k
            self.c += 1
            return True
        return False    

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        
        Running time: O(1).
        """
        if not self.isEmpty():
            self.h = (self.h + 1) % self.k
            self.c -= 1
            return True
        return False        

    def Front(self) -> int:
        """
        Get the front item from the queue.

        Running time: O(1).
        """
        if not self.isEmpty():
            return self.q[self.h]
        return -1
        
    def Rear(self) -> int:
        """
        Get the last item from the queue.

        Running time: O(1).
        """
        if not self.isEmpty():
            return self.q[(self.t - 1) % self.k]
        return -1
        
    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.

        Running time: O(1).
        """
        return self.c == 0
        
    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.

        Running time: O(1).
        """
        return self.c == self.k
