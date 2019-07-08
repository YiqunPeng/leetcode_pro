class Solution:
    def generatePossibleNextMoves(self, s: str) -> List[str]:
    	"""Running Time: O(n) where n is length of s.
    	"""
        r = []
        
        for i in range(1, len(s)):
            if s[i-1] == s[i] == '+':
                t = list(s)
                t[i-1] = t[i] = '-'
                r.append(''.join(t))
                
        return r
 