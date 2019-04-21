class QueueNode:
    
    def __init__(self, v=None, n=None):
        self.val = v
        self.next = n
        

class MyQueue:
    
    def __init__(self):
        """
        Initialize an empty queue.
        """
        self.head = QueueNode()
        self.tail = QueueNode()
        self.head.next = self.tail
        self.length = 0
        
    
    def push(self, x: int) -> None:
        """
        Push element x to the end of queue.
        """
        n_tail = QueueNode(x)
        if self.empty():
            self.head.next = n_tail
        self.tail.next = n_tail
        self.tail = n_tail
        self.length += 1
        
    
    def pop(self) -> int:
        """
        Removes and returns the front element of queue.
        """
        n, v = self.head.next, self.head.next.val
        self.head.next = self.head.next.next
        del n
        self.length -= 1
        return v
    
    
    def top(self) -> int:
        """
        Returns the front element of queue.
        """
        return self.head.next.val
    
    
    def size(self) -> int:
        """
        Returns the size of queue.
        """
        return self.length
    
    
    def empty(self) -> bool:
        """
        Returns if queue is empty.
        """
        return not self.size()


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = MyQueue()
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q.push(x)
        for i in range(self.q.size()-1):
            self.q.push(self.q.pop())
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q.pop()
        

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q.top()
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.q.empty()
