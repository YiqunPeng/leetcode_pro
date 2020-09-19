class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        """Array.

        Running time: O(n) where n is the length of nums.
        """
        f, s, t = None, None, None
        
        for n in nums:
            if f is None or f == n:
                f = n
            elif n > f:
                f, s, t = n, f, s
            else:
                if s is None or s == n:
                    s = n
                elif n > s:
                    s, t = n, s
                else:
                    if t is None or n >= t:
                        t = n

        if t is not None:
            return t
        else:
            return f