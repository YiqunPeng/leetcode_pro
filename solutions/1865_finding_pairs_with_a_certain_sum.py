class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.freq1 = Counter(nums1)
        self.freq2 = Counter(nums2)
        self.nums2 = nums2

    def add(self, index: int, val: int) -> None:
        self.freq2[self.nums2[index]] -= 1
        self.freq2[self.nums2[index]+val] += 1
        self.nums2[index] += val

    def count(self, tot: int) -> int:
        res = 0
        for k in self.freq1:
            res += self.freq1[k] * self.freq2.get(tot - k, 0)
        return res
