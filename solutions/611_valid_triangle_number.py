class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        """Two pointers.

        Running time: O(n^2) where nums is the length of nums.
        """
        nums.sort()
        n = len(nums)
        res = 0
        for i in range(2, n):
            l, r = 0, i - 1
            while l < r:
                if nums[l] + nums[r] <= nums[i]:
                    l += 1
                else:
                    res += r - l
                    r -= 1
        return res
