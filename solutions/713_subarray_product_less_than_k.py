class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """Two pointers.

        Running time: O(n) where n == len(nums).
        """
        if k <= 1:
            return 0
        p = 1
        i = 0
        res = 0
        for j in range(len(nums)):
            p *= nums[j]
            while p >= k:
                p //= nums[i]
                i += 1
            res += j - i + 1
        return res
