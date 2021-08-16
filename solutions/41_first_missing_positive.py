class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """Array.

        Running time: O(n) where n == len(nums).
        """
        nums.append(0)
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n
        for i in range(n):
            v = abs(nums[i])
            if v < n:
                nums[v] = -abs(nums[v])
        for i in range(1, n):
            if nums[i] > 0:
                return i
        return n
