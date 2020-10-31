class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        Array.

        Running time: O(n) where n == len(nums).
        """
        n = len(nums)    
        p = n - 1
        while p > 0 and nums[p] <= nums[p-1]:
            p -= 1
        if p == 0:
            nums.sort()
        else:
            q = p - 1
            while p + 1 < n and (nums[p] == nums[p+1] or nums[p+1] > nums[q]):
                p += 1
            nums[q], nums[p] = nums[p], nums[q]
            l, r = q + 1, n - 1
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
