class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        """Array.

        Running time: O(n) where n is the length of A.
        """
        res = [0] * len(nums)
        p = len(nums) - 1
        l, r = 0, len(nums) - 1
        while p >= 0:
            if abs(nums[l]) >= abs(nums[r]):
                res[p] = nums[l] * nums[l]
                l += 1
            else:
                res[p] = nums[r] * nums[r]
                r -= 1
            p -= 1
        return res
