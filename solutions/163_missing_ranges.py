class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        """Array.

        Running time: O(n) where n == len(nums).
        """
        res = []
        nxt = lower
        for i in range(len(nums)):
            if nums[i] < nxt:
                continue
            if nums[i] == nxt:
                nxt += 1
                continue
            self._append_range(nxt, nums[i] - 1, res)
            nxt = nums[i] + 1
        self._append_range(nxt, upper, res)
        return res
    
    def _append_range(self, lo, hi, res):
        if lo == hi:
            res.append(str(lo))
        elif lo < hi:
            res.append(str(lo) + '->' + str(hi))
