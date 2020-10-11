class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        """Array.

        Running time: O(n) where n is the length of nums.
        """
        c = collections.Counter(nums)
        while c:
            m = min(c.keys())
            for i in range(1, k):
                if c[m+i] < c[m]:
                    return False
            v = c[m]
            for i in range(k):
                c[m+i] -= v
                if c[m+i] == 0:
                    c.pop(m+i)
        return True
