class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """Array.

        Running time: O(n) where n is the length of nums.
        """
        l, r = 1, 1
        n = len(nums)
        res = [1] * n
        for i in range(1, n):
            l *= nums[i-1]
            res[i] = l
        for i in range(n-2, -1, -1):
            r *= nums[i+1]
            res[i] *= r
        return res
