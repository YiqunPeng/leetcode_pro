class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """Array.

        Running time: O(n) where n is the length of nums.
        """
        f, s = None, None
        for num in nums:
            if f is None:
                f = num
            elif num >= f:
                s = f
                f = num
            elif num < f:
                if s is None:
                    s = num
                elif num > s:
                    s = num
        return (f - 1) * (s - 1)
