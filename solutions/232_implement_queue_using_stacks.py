class MyStack:
    
    def __init__(self):
        """
        Initialize an empty stack.
        """
        self.s = []
        
    
    def push(self, x: int) -> None:
        """
        Push element x to the top of stack.
        """
        self.s.append(x)
        
        
    def pop(self) -> int:
        """
        Removes and returns the top element of stack.
        """
        return self.s.pop()
    
    
    def top(self) -> int:
        """
        Returns the value of top element of stack.
        """
        return self.s[-1]
    
    
    def size(self) -> int:
        """
        Returns the number of elements in stack.
        """
        return len(self.s)
    
    
    def empty(self) -> bool:
        """
        Returns if stack is empty.
        """
        return not self.size()


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.a = MyStack()
        self.b = MyStack()
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.a.push(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.b.empty():
            self.move()
        return self.b.pop()
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.b.empty():
            self.move()
        return self.b.top()
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.a.empty() and self.b.empty()
        
    
    def move(self) -> None:
        while not self.a.empty():
            self.b.push(self.a.pop())
