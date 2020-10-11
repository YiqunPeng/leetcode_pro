class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        """Array.

        Running time: O(n) where n == len(A).
        """
        res = []
        s = 0
        for a in A:
            s = s * 2 + a
            if s % 5 == 0:
                s = 0
                res.append(True)
            else:
                res.append(False)
        return res
