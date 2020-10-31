class Solution:
    def generatePossibleNextMoves(self, s: str) -> List[str]:
    	"""Running Time: O(n) where n is length of s.
    	"""
        res = []
        for i in range(len(s) - 1):
            if s[i] == s[i+1] == '+':
                res.append(s[:i] + '--' + s[i+2:])
        return res
 