class FrontMiddleBackQueue:

    def __init__(self):
        self.f = deque()
        self.b = deque()

    def pushFront(self, val: int) -> None:
        self.f.appendleft(val)
        self._balance()

    def pushMiddle(self, val: int) -> None:
        if len(self.f) > len(self.b):
            self.b.appendleft(self.f.pop())
        self.f.append(val)
 
    def pushBack(self, val: int) -> None:
        self.b.append(val)
        self._balance()

    def popFront(self) -> int:
        v = self.f.popleft() if self.f else -1
        self._balance()
        return v

    def popMiddle(self) -> int:
        v = self.f.pop() if self.f else -1
        self._balance()
        return v

    def popBack(self) -> int:
        v = (self.b or self.f or [-1]).pop()
        self._balance()
        return v
    
    def _balance(self):
        if len(self.f) > len(self.b) + 1:
            self.b.appendleft(self.f.pop())
        if len(self.f) < len(self.b):
            self.f.append(self.b.popleft())
