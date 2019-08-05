class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
    	"""Hash table

		Running time: O(n) where n is the length of A.
    	"""
        pb = {b: i for i, b in enumerate(B)}        
        return [pb[a] for a in A]