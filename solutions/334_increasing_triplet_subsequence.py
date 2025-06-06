class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        f, s = float('inf'), float('inf')
        for n in nums:
            if n <= f:
                f = n
            elif n <= s:
                s = n
            else:
                return True
        return False