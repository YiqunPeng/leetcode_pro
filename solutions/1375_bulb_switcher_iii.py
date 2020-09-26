class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        """Array.

        Running time: O(n) where n is the length of light.
        """
        n = len(light)
        p = light[0]
        res = 0
        for i in range(n):
            p = max(p, light[i])
            if p == i + 1:
                res += 1
        return res
