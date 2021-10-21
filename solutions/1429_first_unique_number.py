class FirstUnique:

    def __init__(self, nums: List[int]):
        self.f = Counter(nums)
        self.q = deque(self.f.keys())
            
    def showFirstUnique(self) -> int:
        while self.q and self.f[self.q[0]] > 1:
            self.q.popleft()
        return self.q[0] if self.q else -1

    def add(self, value: int) -> None:
        if value not in self.f:
            self.f[value] = 1
            self.q.append(value)
        else:
            self.f[value] += 1
