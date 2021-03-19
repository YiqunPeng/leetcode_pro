class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
    	"""Hash table.

    	Running time: O(n) where n is the length of t.
    	"""
        cs = Counter(s)
        ct = Counter(t)
        for k in ct:
            if k not in cs or cs[k] != ct[k]:
                return k
