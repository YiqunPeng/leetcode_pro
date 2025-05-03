class NumArray:

    def __init__(self, nums: List[int]):
        self.pre_sum = [0] * (len(nums) + 1)
        for i in range(1, len(self.pre_sum)):
            self.pre_sum[i] = self.pre_sum[i-1] + nums[i-1]

    def sumRange(self, left: int, right: int) -> int:
        return self.pre_sum[right+1] - self.pre_sum[left]