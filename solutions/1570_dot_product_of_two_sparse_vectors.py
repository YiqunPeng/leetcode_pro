class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        p1 = 0
        p2 = 0
        res = 0
        while p1 < len(self.nums) and p2 < len(vec.nums):
            if self.nums[p1] == 0:
                p1 += 1
                continue
            if vec.nums[p2] == 0:
                p2 += 1
                continue
            if p1 == p2:
                res += self.nums[p1] * vec.nums[p2]
                p1 += 1
                p2 += 1
            elif p1 < p2:
                p1 += 1
            else:
                p2 += 1
        return res
