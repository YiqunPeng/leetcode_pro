class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """Array.

        Running time: O(n) where n == len(nums).
        """
        n = len(nums)
        if n == 1:
            return True
        m = nums[0]
        p = 0
        while p <= m:
            m = max(m, p + nums[p])
            if m >= n - 1:
                return True
            p += 1
        return False
