class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.a, self.b = [], []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.a.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.b:
            self.move()
        return self.b.pop()
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.b:
            self.move()
        return self.b[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.a and not self.b
        
    
    def move(self) -> None:
        while self.a:
            self.b.append(self.a.pop())
