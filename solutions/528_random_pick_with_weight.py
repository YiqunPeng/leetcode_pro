class Solution:

    def __init__(self, w: List[int]):
        self.accum = [w[0]]
        for i in range(1, len(w)):
            self.accum.append(self.accum[-1] + w[i])

    def pickIndex(self) -> int:
        r = random.randint(1, self.acc[-1])
        return bisect.bisect_left(self.acc, r)
