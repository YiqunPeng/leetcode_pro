class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        """Two pointers.

        Running time: O(n) where n is the length of S.
        """
        l, r = 0, 0
        res = []
        while r < len(s):
            while r < len(s) and s[l] == s[r]:
                r += 1
            if r - l > 2:
                res.append([l, r - 1])
            l = r
        return res
        