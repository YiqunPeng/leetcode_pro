class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
    	"""Hash set.

		Running time: O(n) where n is the total length of J plus S.
    	"""
        j = set(J)
        
        ret = 0
        for s in S:
            if s in j:
                ret += 1      
        return ret
