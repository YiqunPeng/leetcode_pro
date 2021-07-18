class RangeModule:

    def __init__(self):
        self.ranges = []
        
    def _find_overlap(self, left, right):
        n = len(self.ranges)
        l = 0
        while l < n and self.ranges[l][1] < left:
            l += 1
        r = n - 1
        while r >= 0 and self.ranges[r][0] > right:
            r -= 1
        return l, r

    def addRange(self, left: int, right: int) -> None:
        n = len(self.ranges)
        l, r = self._find_overlap(left, right)
        if l <= r:
            left = min(left, self.ranges[l][0])
            right = max(right, self.ranges[r][1])
        self.ranges[l:r+1] = [[left, right]]

    def queryRange(self, left: int, right: int) -> bool:
        if not self.ranges:
            return False
        vals = [i[0] for i in self.ranges]
        idx = bisect.bisect_left(vals, left + 1) - 1
        return self.ranges[idx][0] <= left and self.ranges[idx][1] >= right

    def removeRange(self, left: int, right: int) -> None:
        l, r = self._find_overlap(left, right)
        fractions = []
        for i in range(l, r + 1):
            if self.ranges[i][0] < left:
                fractions.append([self.ranges[i][0], left])
            if self.ranges[i][1] > right:
                fractions.append([right, self.ranges[i][1]])
        self.ranges[l:r+1] = fractions
