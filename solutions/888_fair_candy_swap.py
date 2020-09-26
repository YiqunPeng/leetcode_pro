class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
    	"""Hash table.

    	Running time: O(n) where n is the length of A plus the length of B. 
    	"""
        d = sum(A) - sum(B)
        a = set(A)
        b = set(B)
        for i in a:
            if (i - d // 2) in b:
                return [i, i - d // 2]
 