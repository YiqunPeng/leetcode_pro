class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
    	"""Hash set.

		Running time: O(n) where n is the total length of J plus S.
    	"""
        j = set(J)
        return len([i for i in S if i in j])
