class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        """Array.

        Running time: O(n) where n == len(nums).
        """
        if not nums:
            return [self._get_range(lower, upper)]
        p = 0
        while nums[p] < lower:
            p += 1
        res = []
        r = self._get_range(lower, nums[p] - 1)
        if r:
            res.append(r)
        for i in range(p + 1, len(nums)):
            if nums[i] > upper:
                r = self._get_range(nums[i-1] + 1, upper)
                if r:
                    res.append(r)
                return res
            if nums[i] != nums[i-1]:
                r = self._get_range(nums[i-1] + 1, nums[i] - 1)
                if r:
                    res.append(r)
        r = self._get_range(nums[-1] + 1, upper)
        if r:
            res.append(r)
        return res
            
        
    def _get_range(self, l, u):
        if l > u:
            return ""
        elif l == u:
            return str(l)
        else:
            return str(l) + '->' + str(u)
