class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        """Presum array.
        """
        n = len(nums)
        m = sum(nums) % p
        pres = 0
        d = {0: -1}
        res = n
        for i in range(n):
            pres = (pres + nums[i]) % p
            d[pres] = i
            if (pres - m) % p in d:
                res = min(res, i - d[(pres-m)%p])
        return res if res < n else -1
