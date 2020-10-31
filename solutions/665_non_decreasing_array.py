class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        """Array.

        Running time: O(n) where n == len(nums).
        """
        na, nb = nums[:], nums[:]
        c = 1
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                if c == 0:
                    return False
                c -= 1
                na[i] = na[i-1]
                nb[i-1] = nb[i]
        return c == 1 or self._is_non_decreasing(na) or self._is_non_decreasing(nb)
    
    def _is_non_decreasing(self, arr):
        for i in range(1, len(arr)):
            if arr[i] < arr[i-1]:
                return False
        return True
