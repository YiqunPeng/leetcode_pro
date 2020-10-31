class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        """Prefix array.

        Running time: O(n) where n == len(nums).
        """
        n = len(nums)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i+1] = pref[i] + nums[i]
        if pref[-1] < s:
            return 0
        i = 0
        res = n
        for j in range(1, n + 1):
            while pref[j] - pref[i] >= s:
                i += 1
                res = min(res, j - i + 1)
        return res
