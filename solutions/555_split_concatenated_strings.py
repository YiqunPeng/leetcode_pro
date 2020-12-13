class Solution:
    def splitLoopedString(self, strs: List[str]) -> str:
    	"""String.

    	Running time: O(n*k) where n == len(strs) and k is the maximum length of items in strs.
    	"""
        a = [max(s, s[::-1]) for s in strs]
        res = ''
        for i, s in enumerate(a):
            t = ''.join(a[i+1:] + a[:i])
            for j in [s, s[::-1]]:
                for k in range(1, len(j) + 1):
                    res = max(res, j[k:] + t + j[:k])
        return res
