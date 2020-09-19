class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
    	"""Hash table.

    	Running time: O(n) where n is the length of t.
    	"""
        sc = collections.Counter(s)
        tc = collections.Counter(t)
        
        for k in tc.keys():
            if k not in sc or sc[k] != tc[k]:
                return k