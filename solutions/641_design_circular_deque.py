class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        
        Running Time: O(1).
        """
        self.deque = [0] * k
        self.front = None
        self.last = None
        self.k = k
        

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        
        Running Time: O(1).
        """
        if self.isFull():
            return False
        
        if self.isEmpty():
            self.deque[0] = value
            self.front = 0
            self.last = 1
        else:
            self.front = (self.front - 1) % self.k
            self.deque[self.front] = value
        
        return True
    

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        
        Running Time: O(1).
        """
        if self.isFull():
            return False
        
        if self.isEmpty():
            self.deque[0] = value
            self.front = 0
            self.last = 1
        else:    
            self.deque[self.last] = value
            self.last = (self.last + 1) % self.k
            
        return True
        

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        
        Running Time: O(1).
        """
        if self.isEmpty():
            return False
        
        if (self.front + 1) % self.k == self.last:
            self.front = self.last = None
        else:
            self.front = (self.front + 1) % self.k
            
        return True
        

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        
        Running Time: O(1).
        """
        if self.isEmpty():
            return False
        
        if (self.front + 1) % self.k == self.last:
            self.front = self.last = None
        else:
            self.last = (self.last - 1) % self.k
            
        return True
        

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        
        Running Time: O(1).
        """
        return -1 if self.isEmpty() else self.deque[self.front]
        

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        
        Running Time: O(1).
        """
        return -1 if self.isEmpty() else self.deque[(self.last - 1) % self.k] 
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.

        Running Time: O(1).
        """
        return self.front == self.last == None
        

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.

        Running Time: O(1).
        """
        return self.front == self.last and self.front is not None
