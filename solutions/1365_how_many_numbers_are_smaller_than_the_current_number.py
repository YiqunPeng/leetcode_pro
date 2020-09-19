class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        """Sort. Hash table.

        Running time: O(nlogn) where n is the length of nums.
        """
        n = len(nums)
        res = [0] * n
        pos = {}
        for i, num in enumerate(nums):
            if num in pos:
                pos[num].append(i)
            else:
                pos[num] = [i]
        sorted_nums = sorted(nums)
        for i in range(1, n):
            if sorted_nums[i] == sorted_nums[i-1]:
                continue
            for v in pos[sorted_nums[i]]:
                res[v] = i
        return res
