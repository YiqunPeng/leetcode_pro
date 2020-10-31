class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """Two pointers.

        Running time: O(n^2) where n == len(nums).
        """
        nums.sort()
        n = len(nums)
        res = sys.maxsize
        for i in range(n - 2):
            l, r = i + 1, n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == target:
                    return s
                if abs(s - target) < abs(res - target):
                    res = s
                if s > target:
                    r -= 1
                else:
                    l += 1
        return res
