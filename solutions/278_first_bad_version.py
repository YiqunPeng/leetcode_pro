class Solution:
    def firstBadVersion(self, n):
        l, r = 1, n + 1
        while l < r:
            m = (l + r) // 2
            if isBadVersion(m):
                r = m
            else:
                l = m + 1
        return l
