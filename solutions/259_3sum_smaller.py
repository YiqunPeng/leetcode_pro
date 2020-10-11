class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        """Two pointers.

        Running time: O(n) where n == len(nums).
        """
        nums.sort()
        n = len(nums)
        res = 0
        for i in range(n):
            t = target - nums[i]
            l, r = i + 1, n - 1
            while l < r:
                if nums[l] + nums[r] < t:
                    res += r - l
                    l += 1
                else:
                    r -= 1
        return res
