class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        """Array.

        Running time: O(n) where n is the length of nums.
        """
        f, s, t = None, None, None
        for n in nums:
            if n == f or n == s or n == t:
                continue
            if f is None:
                f = n
            elif n > f:
                f, s, t = n, f, s
            else:
                if s is None:
                    s = n
                elif n >= s:
                    s, t = n, s
                else:
                    if t is None:
                        t = n
                    elif n >= t:
                        t = n
        return t if t is not None else f
