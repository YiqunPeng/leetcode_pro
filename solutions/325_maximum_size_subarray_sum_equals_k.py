class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        """Hash table.
        """
        d = {0: -1}
        pres = 0
        res = 0
        for i in range(len(nums)):
            pres += nums[i]
            if pres - k in d:
                res = max(res, i - d[pres - k])
            if pres not in d:
                d[pres] = i
        return res
