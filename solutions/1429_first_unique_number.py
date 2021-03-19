class FirstUnique:

    def __init__(self, nums: List[int]):
        self.s = collections.deque(nums)
        self.f = collections.Counter(nums)

    def showFirstUnique(self) -> int:
        while self.s and self.f[self.s[0]] != 1:
            self.s.popleft()
        return self.s[0] if self.s else -1

    def add(self, value: int) -> None:
        self.s.append(value)
        self.f[value] += 1
