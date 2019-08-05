class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
    	"""Hash table.

    	Running time: O(n) where n is the length of A plus the length of B. 
    	"""
        a_s, b_s = sum(A), sum(B)
        a, b = set(A), set(B)
        
        avg = (a_s + b_s) // 2
        
        for i in a:
            if avg - a_s + i in b:
                return i, avg - a_s + i
 