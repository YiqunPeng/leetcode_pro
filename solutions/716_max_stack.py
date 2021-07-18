class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max = None
        self.st = []

    def push(self, x: int) -> None:
        if self.max is None or self.max <= x:
            self.st.append(self.max)
            self.max = x
        self.st.append(x)

    def pop(self) -> int:
        v = self.st.pop()
        if v == self.max:
            self.max = self.st.pop()
        return v

    def top(self) -> int:
        return self.st[-1]

    def peekMax(self) -> int:
        return self.max

    def popMax(self) -> int:
        temp = []
        while self.st and self.st[-1] != self.max:
            temp.append(self.pop())
        v = self.pop()
        while temp:
            self.push(temp.pop())
        return v
