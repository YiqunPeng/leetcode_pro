class Solution:
    def sumOfDigits(self, A: List[int]) -> int:
    	"""Math.

    	Running time: O(n) where n is the length of A.
    	"""
        min_v = min(A)
        
        s = 0
        while min_v:
            s += min_v % 10
            min_v //= 10
            
        return 1 - s % 2