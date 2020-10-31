class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        """Array.

        Running time: O(n) where n == len(arrays).
        """
        n = len(arrays)
        mav, maa = arrays[0][-1], 0
        miv, mia = arrays[0][0], 0
        for i in range(n):
            if arrays[i][0] < miv:
                miv = arrays[i][0]
                mia = i
            if arrays[i][-1] > mav:
                mav = arrays[i][-1]
                maa = i
        if mia != maa:
            return mav - miv
        m = min([arrays[i][0] for i in range(n) if i != mia])
        d = mav - m
        m = max([arrays[i][-1] for i in range(n) if i != maa])
        return max(d, m - miv)
