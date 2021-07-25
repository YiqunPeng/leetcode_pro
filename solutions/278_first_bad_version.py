class Solution:
    def firstBadVersion(self, n):
        lo = 1
        hi = n
        while lo <= hi:
            mi = (lo + hi) // 2
            bad = isBadVersion(mi)
            if mi == 1 and bad or mi > 1 and bad and not isBadVersion(mi-1):
                return mi
            if not bad:
                lo = mi + 1
            else:
                hi = mi - 1
