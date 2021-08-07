class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        """Sliding window.

        Running time: O(n) where n == len(nums).
        """
        res = len(nums) + 1
        i = 0
        s = 0
        for j in range(0, len(nums)):
            s += nums[j]
            if s >= target:
                while i < j and s - nums[i] >= target:
                    s -= nums[i]
                    i += 1
                res = min(j - i + 1, res)
                s -= nums[i]
                i += 1
        return res if res <= len(nums) else 0
