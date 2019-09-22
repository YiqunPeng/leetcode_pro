class Solution:
    def removeDuplicates(self, S: str) -> str:
    	"""Stack.

    	Running time: O(n) where n is the length of S.
    	"""
        s = []
        
        for c in S:
            if not s or s[-1] != c:
                s.append(c)
            else:
                while s and s[-1] == c:
                    s.pop()
        
        return ''.join(s)