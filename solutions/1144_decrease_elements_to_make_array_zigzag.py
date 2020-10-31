class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        """Array.

        Running time: O(n) where n == len(nums).
        """
        nums.append(sys.maxsize)
        c = 0
        for i in range(1, len(nums) - 1, 2):
            m = min(nums[i-1], nums[i+1])
            c += max(0, nums[i] - m + 1)
        res = c
        c = 0
        nums = [sys.maxsize] + nums
        for i in range(1, len(nums) - 1, 2):
            m = min(nums[i-1], nums[i+1])
            c += max(0, nums[i] - m + 1)
        return min(res, c)
