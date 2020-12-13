class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        """Sort.

        Running time: O(nlogn) where n == len(timePoints).
        """
        m = []
        for t in timePoints:
            hr, mi = t.split(':', 1)
            m.append(int(hr) * 60 + int(mi))
        m.sort()
        m.append(m[0] + 24 * 60)
        res = 24 * 60
        for i in range(1, len(m)):
            res = min(res, m[i] - m[i-1])
        return res
